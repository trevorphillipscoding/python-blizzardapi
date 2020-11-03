from .wow_game_data_api import GameDataApi
from .wow_profile_api import ProfileApi


class WowApi:
    def __init__(self, access_token):
        self.game_data = GameDataApi(access_token)
        self.profile = ProfileApi(access_token)
