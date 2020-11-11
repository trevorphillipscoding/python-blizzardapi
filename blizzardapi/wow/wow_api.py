from .wow_game_data_api import WowGameDataApi
from .wow_profile_api import WowProfileApi


class WowApi:
    """WoW API class.

    Attributes:
        client_id: A client id supplied by Blizzard.
        client_secret: A client secret supplied by Blizzard.
    """

    def __init__(self, client_id, client_secret):
        """Inits WowApi"""
        self.game_data = WowGameDataApi(client_id, client_secret)
        self.profile = WowProfileApi(client_id, client_secret)
