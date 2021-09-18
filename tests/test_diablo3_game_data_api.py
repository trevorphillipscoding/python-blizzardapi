from blizzardapi import BlizzardApi


class TestDiablo3GameDataApi:
    def setup(self):
        self.api = BlizzardApi("client_id", "client_secret")
        self.api.diablo3.game_data._access_token = "access_token"

    # D3

    def test_get_season_index(self, success_response_mock):
        self.api.diablo3.game_data.get_season_index("us")
        params = {
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/d3/season/", params=params
        )

    def test_get_season(self, success_response_mock):
        self.api.diablo3.game_data.get_season("us", 1)
        params = {
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/d3/season/1", params=params
        )

    def test_get_season_leaderboard(self, success_response_mock):
        self.api.diablo3.game_data.get_season_leaderboard("us", 1, "achievement-points")
        params = {
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/d3/season/1/leaderboard/achievement-points",
            params=params,
        )

    def test_get_era_index(self, success_response_mock):
        self.api.diablo3.game_data.get_era_index("us")
        params = {
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/d3/era/", params=params
        )

    def test_get_era(self, success_response_mock):
        self.api.diablo3.game_data.get_era("us", 1)
        params = {
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/d3/era/1", params=params
        )

    def test_get_era_leaderboard(self, success_response_mock):
        self.api.diablo3.game_data.get_era_leaderboard("us", 1, "rift-barbarian")
        params = {
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/d3/era/1/leaderboard/rift-barbarian",
            params=params,
        )
