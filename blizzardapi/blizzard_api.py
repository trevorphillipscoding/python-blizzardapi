from .battlenet_api import BattlenetApi
from .diablo3_api import Diablo3Api
from .wow_api import WowApi


class BlizzardApi:
    def __init__(self, client_id, client_secret):
        self.battlenet = BattlenetApi(client_id, client_secret)
        self.diablo3 = Diablo3Api(client_id, client_secret)
        self.wow = WowApi(client_id, client_secret)
