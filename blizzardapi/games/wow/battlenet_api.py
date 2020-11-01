from ...api import Api


class BattlenetApi(Api):
    """All Battlenet API methods"""

    def __init__(self, region, client_id, client_secret, access_token):
        super().__init__(region, client_id, client_secret, access_token)

    # User Authentication

    def get_user_info(self):
        """
         Battlenet API - Returns basic information about the user
         associated with the current bearer token.
        """
        resource = f"/oauth/token"
        return super().get_resource(resource)
