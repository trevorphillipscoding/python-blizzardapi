from .battlenet_oauth_api import BattlenetOauthApi


class BattlenetApi:
    def __init__(self, client_id, client_secret):
        self.oauth = BattlenetOauthApi(client_id, client_secret)
