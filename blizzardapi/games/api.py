import requests
from requests.exceptions import RequestException

from ..exceptions import BlizzardApiRequestException


class Api:
    def __init__(self, access_token, region):
        self._access_token = access_token
        self.region = region

        self._api_url = "https://{0}.api.blizzard.com{1}"
        self._api_url_cn = "https://gateway.battlenet.com.cn{0}"

        self._session = requests.Session()

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
        query_params["access_token"] = self._access_token
        return self._request(url, **query_params)

    def _format_api_url(self, resource):
        if self.region == "cn":
            url = self._api_url_cn.format(resource)
        else:
            url = self._api_url.format(self.region, resource)

        return url

    def get_resource(self, resource, **query_params):
        url = self._format_api_url(resource)
        return self._request_handler(url, **query_params)
