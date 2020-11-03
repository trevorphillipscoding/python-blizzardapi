from urllib import parse

from .api import Api


class BattlenetOauthApi(Api):
    """All OAuth API methods"""

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    def _add_params_to_url(self, url, query_params):
        return f"{url}?{parse.urlencode(query_params)}"

    # User Authentication

    def authorization_request(self, region, redirect_uri, scope, state):
        """
        User Authentication - Returns a string url that is used to request authorization from a user.
        """
        resource = f"/oauth/authorize"
        query_params = {
            "client_id": self.client_id,
            "redirect_uri": redirect_uri,
            "response_type": "code",
            "scope": scope,
            "state": state,
        }
        url = self.format_oauth_url(resource, region)
        return self._add_params_to_url(url, query_params)
