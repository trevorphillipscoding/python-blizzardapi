import requests
from requests.exceptions import RequestException

from .exceptions import BlizzardApiRequestException


class Api:
    def __init__(self, region, client_id, client_secret, access_token):
        self.region = region
        self._client_id = client_id
        self._client_secret = client_secret
        self._access_token = access_token

        self._base_url = "https://{0}.api.blizzard.com{1}"
        self._base_url_cn = "https://gateway.battlenet.com.cn{0}"

        self._oauth_url = "https://{0}.battle.net{1}"
        self._oauth_url_cn = "https://www.battlenet.com.cn{0}"

        self._session = requests.Session()

    def _get_client_credentials(self):
        if self.region == "cn":
            url = self._oauth_url_cn.format("/oauth/token")
        else:
            url = self._oauth_url.format(self.region, "/oauth/token")

        json = self._oauth_request(url, grant_type="client_credentials")

        self._access_token = json["access_token"]

    def _oauth_request(self, url, **query_params):
        try:
            response = self._session.post(url, params=query_params, auth=(
                self._client_id, self._client_secret))
        except RequestException as e:
            raise BlizzardApiRequestException(str(e))

        if not response.ok:
            msg = f"Invalid response - {response.status_code} for {response.url}"
            raise BlizzardApiRequestException(msg)

        try:
            json = response.json()
        except Exception as e:
            raise BlizzardApiRequestException(str(e))

        return json

    def _request(self, url, **query_params):
        try:
            response = self._session.get(url, params=query_params)
        except RequestException as e:
            raise BlizzardApiRequestException(str(e))

        if not response.ok:
            msg = f"Invalid response - {response.status_code} for {response.url}"
            raise BlizzardApiRequestException(msg)

        try:
            json = response.json()
        except Exception as e:
            raise BlizzardApiRequestException(str(e))

        return json

    def _request_handler(self, url, **query_params):
        if self._access_token is None:
            self._get_client_credentials()
            return self._request_handler(url, **query_params)

        query_params["access_token"] = self._access_token
        json = self._request(url, **query_params)

        return json

    def get_resource(self, resource, **query_params):
        if self.region == "cn":
            url = self._base_url_cn.format(resource)
        else:
            url = self._base_url.format(self.region, resource)
        return self._request_handler(url, **query_params)
