from .hearthstone_game_data_api import HearthstoneGameDataApi


class HearthstoneApi:
    def __init__(self, client_id, client_secret):
        self.game_data = HearthstoneGameDataApi(client_id, client_secret)
