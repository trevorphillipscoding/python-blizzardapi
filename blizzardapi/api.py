import requests
from requests.exceptions import RequestException

from .exceptions import BlizzardApiRequestException


class Api:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self._client_secret = client_secret
        self._access_token = None

        self._oauth_url = "https://{0}.battle.net{1}"
        self._oauth_url_cn = "https://www.battlenet.com.cn{0}"

        self._api_url = "https://{0}.api.blizzard.com{1}"
        self._api_url_cn = "https://gateway.battlenet.com.cn{0}"

        self._session = requests.Session()

    def format_oauth_url(self, resource, region):
        if region == "cn":
            url = self._oauth_url_cn.format(resource)
        else:
            url = self._oauth_url.format(region, resource)

        return url

    def _get_client_token(self, region):
        url = self.format_oauth_url("/oauth/token", region)
        query_params = {"grant_type": "client_credentials"}

        try:
            response = self._session.post(
                url,
                params=query_params,
                auth=(self.client_id, self._client_secret),
            )
        except RequestException as e:
            raise BlizzardApiRequestException(str(e))

        return self._response_handler(response)

    def _response_handler(self, response):
        if not response.ok:
            msg = (
                f"Invalid response - {response.status_code} for {response.url}"
            )
            raise BlizzardApiRequestException(msg)

        try:
            json = response.json()
        except Exception as e:
            raise BlizzardApiRequestException(str(e))

        return json

    def _format_api_url(self, resource, region):
        if region == "cn":
            url = self._api_url_cn.format(resource)
        else:
            url = self._api_url.format(region, resource)

        return url

    def _request_handler(self, resource, region, query_params):
        if self._access_token is None:
            json = self._get_client_token(region)
            self._access_token = json["access_token"]

        if query_params.get("access_token") is None:
            query_params["access_token"] = self._access_token

        url = self._format_api_url(resource, region)

        try:
            response = self._session.get(url, params=query_params)
        except RequestException as e:
            raise BlizzardApiRequestException(str(e))

        return self._response_handler(response)

    def get_resource(self, resource, region, query_params):
        return self._request_handler(resource, region, query_params)
