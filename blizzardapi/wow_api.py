from .wow_game_data_api import GameDataApi
from .wow_profile_api import ProfileApi


class WowApi:
    def __init__(self, client_id, client_secret):
        self.game_data = GameDataApi(client_id, client_secret)
        self.profile = ProfileApi(client_id, client_secret)
