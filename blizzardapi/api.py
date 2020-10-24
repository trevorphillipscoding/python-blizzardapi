import requests
from requests.exceptions import RequestException

from .exceptions import (
    BlizzardApiClientException,
    BlizzardApiOAuthException,
    BlizzardApiRequestException,
)
from .mixins import GameDataMixin


class BlizzardApi(GameDataMixin):
    def __init__(
        self,
        client_id=None,
        client_secret=None,
        access_token=None,
        region="us",
        locale="en_US",
    ):
        self._client_id = client_id
        self._client_secret = client_secret
        self._access_token = access_token
        self._region = region
        self._locale = locale

        self.api_url = "https://{0}.api.blizzard.com{1}"
        self.api_cn_url = "https://gateway.battlenet.com.cn{0}"
        self.oauth_url = "https://{0}.battle.net{1}"
        self.oauth_cn_url = "https://www.battlenet.com.cn{0}"
        self._session = requests.Session()

        self._is_valid_client()

    def _is_valid_client(self):
        if (
            self._client_id is None
            and self._client_secret is None
            and self._access_token is None
        ):
            msg = "You must initialize the client with a client id/client secret or an access token."
            raise BlizzardApiClientException(msg)

        elif self._client_id is None and self._client_secret is not None:
            msg = "You must initialize the client with a client id to make this work!"
            raise BlizzardApiClientException(msg)

        elif self._client_id is not None and self._client_secret is None:
            msg = (
                "You must initialize the client with a client secret to make this work!"
            )
            raise BlizzardApiClientException(msg)

    def _get_client_credentials(self):
        if self._region == "cn":
            url = self.oauth_cn_url.format(self._region, "/oauth/token")
        else:
            url = self.oauth_url.format(self._region, "/oauth/token")
        filters = {
            "grant_type": "client_credentials",
            "client_id": self._client_id,
            "client_secret": self._client_secret,
        }

        try:
            response = self._session.get(url, params=filters)
        except RequestException as e:
            raise BlizzardApiOAuthException(str(e))

        if not response.ok:
            msg = "Invalid response - {0} for {1}".format(
                response.status_code, response.url
            )
            raise BlizzardApiOAuthException(msg)

        try:
            json = response.json()
        except Exception as e:
            raise BlizzardApiOAuthException(str(e))

        self._access_token = json["access_token"]

    def _request_handler(self, url, **filters):
        if self._access_token is None:
            self._get_client_credentials()
            return self._request_handler(url, **filters)

        filters["locale"] = self._locale
        filters["access_token"] = self._access_token

        try:
            response = self._session.get(url, params=filters)
        except RequestException as e:
            raise BlizzardApiRequestException(str(e))

        if not response.ok:
            msg = "Invalid response - {0} for {1}".format(
                response.status_code, response.url
            )
            raise BlizzardApiRequestException(msg)

        try:
            json = response.json()
        except Exception as e:
            raise BlizzardApiRequestException(str(e))

        return json

    def get_data_resource(self, url):
        return self._request_handler(url)

    def get_resource(self, resource, namespace, *args):
        resource = resource.format(*args)
        namespace = namespace.format(self._region)

        if self._region == "cn":
            url = self.api_cn_url.format(resource)
        else:
            url = self.api_url.format(self._region, resource)
        return self._request_handler(url, namespace=namespace)
