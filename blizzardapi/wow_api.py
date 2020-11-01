from .games.wow.battlenet_api import BattlenetApi
from .games.wow.game_data_api import GameDataApi
from .games.wow.profile_api import ProfileApi


class WowApi:
    def __init__(self, region="us", locale="en_US", client_id=None, client_secret=None, access_token=None):
        self.battlenet = BattlenetApi(
            region, client_id, client_secret, access_token)
        self.game_data = GameDataApi(
            region, locale, client_id, client_secret, access_token)
        self.profile = ProfileApi(
            region, locale, client_id, client_secret, access_token)
