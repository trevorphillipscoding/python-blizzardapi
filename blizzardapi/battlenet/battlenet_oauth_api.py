from urllib import parse

from ..api import Api


class BattlenetOauthApi(Api):
    """All OAuth API methods"""

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    # User Authentication

    def get_user_info(self, region, access_token):
        """
        User Authentication - Returns basic information about the user associated with the current bearer token.
        """
        resource = "/oauth/userinfo"
        query_params = {
            "access_token": access_token,
        }
        return super().get_oauth_resource(resource, region, query_params)
