from blizzardapi import BlizzardApi


class TestDiablo3CommunityApi:
    def setup(self):
        self.api = BlizzardApi("client_id", "client_secret")
        self.api.diablo3.community._access_token = "access_token"

    # D3 Act API

    def test_get_act_index(self, success_response_mock):
        self.api.diablo3.community.get_act_index("us", "en_US")
        params = {
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/d3/data/act",
            params=params,
        )

    def test_get_act(self, success_response_mock):
        self.api.diablo3.community.get_act("us", "en_US", 1)
        params = {
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/d3/data/act/1",
            params=params,
        )

    # D3 Artisan and Recipe API

    def test_get_artisan(self, success_response_mock):
        self.api.diablo3.community.get_artisan("us", "en_US", "blacksmith")
        params = {
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/d3/data/artisan/blacksmith",
            params=params,
        )

    def test_get_recipe(self, success_response_mock):
        self.api.diablo3.community.get_recipe(
            "us", "en_US", "blacksmith", "apprentice-flamberge"
        )
        params = {
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/d3/data/artisan/blacksmith/recipe/apprentice-flamberge",
            params=params,
        )

    # D3 Follower API

    def test_get_follower(self, success_response_mock):
        self.api.diablo3.community.get_follower("us", "en_US", "templar")
        params = {
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/d3/data/follower/templar",
            params=params,
        )

    # D3 Character Class and Skill API

    def test_get_character_class(self, success_response_mock):
        self.api.diablo3.community.get_character_class(
            "us", "en_US", "barbarian"
        )
        params = {
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/d3/data/hero/barbarian",
            params=params,
        )

    def test_get_api_skill(self, success_response_mock):
        self.api.diablo3.community.get_api_skill(
            "us", "en_US", "barbarian", "bash"
        )
        params = {
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/d3/data/hero/barbarian/skill/bash",
            params=params,
        )

    # D3 Item Type API

    def test_get_item_type_index(self, success_response_mock):
        self.api.diablo3.community.get_item_type_index("us", "en_US")
        params = {
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/d3/data/item-type",
            params=params,
        )

    def test_get_item_type(self, success_response_mock):
        self.api.diablo3.community.get_item_type("us", "en_US", "sword2h")
        params = {
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/d3/data/item-type/sword2h",
            params=params,
        )

    # D3 Item API

    def test_get_item(self, success_response_mock):
        self.api.diablo3.community.get_item(
            "us", "en_US", "corrupted-ashbringer-Unique_Sword_2H_104_x1"
        )
        params = {
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/d3/data/item/corrupted-ashbringer-Unique_Sword_2H_104_x1",
            params=params,
        )

    # D3 Profile API

    def test_get_api_account(self, success_response_mock):
        self.api.diablo3.community.get_api_account(
            "us", "en_US", "Battletag#1234"
        )
        params = {
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/d3/profile/Battletag#1234/",
            params=params,
        )

    def test_get_api_hero(self, success_response_mock):
        self.api.diablo3.community.get_api_hero(
            "us", "en_US", "Battletag#1234", 1
        )
        params = {
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/d3/profile/Battletag#1234/hero/1",
            params=params,
        )

    def test_get_api_detailed_hero_items(self, success_response_mock):
        self.api.diablo3.community.get_api_detailed_hero_items(
            "us", "en_US", "Battletag#1234", 1
        )
        params = {
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/d3/profile/Battletag#1234/hero/1/items",
            params=params,
        )

    def test_get_api_detailed_follower_items(self, success_response_mock):
        self.api.diablo3.community.get_api_detailed_follower_items(
            "us", "en_US", "Battletag#1234", 1
        )
        params = {
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/d3/profile/Battletag#1234/hero/1/follower-items",
            params=params,
        )
