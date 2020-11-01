from .games.wow.game_data_api import GameDataApi
from .games.wow.profile_api import ProfileApi


class WowApi:
    def __init__(self, access_token, region, locale):
        self.game_data = GameDataApi(access_token, region, locale)
        self.profile = ProfileApi(access_token, region, locale)
