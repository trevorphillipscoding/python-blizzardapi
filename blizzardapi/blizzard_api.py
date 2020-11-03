from .wow_api import WowApi


class BlizzardApi:
    def __init__(self, client_id, client_secret):
        self.wow = WowApi(client_id, client_secret)
