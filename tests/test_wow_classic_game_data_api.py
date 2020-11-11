from blizzardapi import BlizzardApi


class TestWowClassicGameDataApi:
    def setup(self):
        self.api = BlizzardApi("client_id", "client_secret")
        self.api.wow.game_data._access_token = "access_token"

    # Connected Realm API

    def test_get_connected_realms_index(self, success_response_mock):
        self.api.wow.game_data.get_connected_realms_index(
            "us", "en_US", is_classic=True
        )
        params = {
            "namespace": "dynamic-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/connected-realm/index",
            params=params,
        )

    def test_get_connected_realm(self, success_response_mock):
        self.api.wow.game_data.get_connected_realm(
            "us", "en_US", 1, is_classic=True
        )
        params = {
            "namespace": "dynamic-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/connected-realm/1",
            params=params,
        )

    # Creature API

    def test_get_creature_families_index(self, success_response_mock):
        self.api.wow.game_data.get_creature_families_index(
            "us", "en_US", is_classic=True
        )
        params = {
            "namespace": "static-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/creature-family/index",
            params=params,
        )

    def test_get_creature_family(self, success_response_mock):
        self.api.wow.game_data.get_creature_family(
            "us", "en_US", 1, is_classic=True
        )
        params = {
            "namespace": "static-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/creature-family/1",
            params=params,
        )

    def test_get_creature_types_index(self, success_response_mock):
        self.api.wow.game_data.get_creature_types_index(
            "us", "en_US", is_classic=True
        )
        params = {
            "namespace": "static-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/creature-type/index",
            params=params,
        )

    def test_get_creature_type(self, success_response_mock):
        self.api.wow.game_data.get_creature_type(
            "us", "en_US", 1, is_classic=True
        )
        params = {
            "namespace": "static-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/creature-type/1",
            params=params,
        )

    def test_get_creature(self, success_response_mock):
        self.api.wow.game_data.get_creature("us", "en_US", 1, is_classic=True)
        params = {
            "namespace": "static-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/creature/1", params=params
        )

    def test_get_creature_display_media(self, success_response_mock):
        self.api.wow.game_data.get_creature_display_media(
            "us", "en_US", 1, is_classic=True
        )
        params = {
            "namespace": "static-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/creature-display/1",
            params=params,
        )

    def test_get_creature_family_media(self, success_response_mock):
        self.api.wow.game_data.get_creature_family_media(
            "us", "en_US", 1, is_classic=True
        )
        params = {
            "namespace": "static-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/creature-family/1",
            params=params,
        )

    # Guild Crest API

    def test_get_guild_crest_components_index(self, success_response_mock):
        self.api.wow.game_data.get_guild_crest_components_index(
            "us", "en_US", is_classic=True
        )
        params = {
            "namespace": "static-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/guild-crest/index",
            params=params,
        )

    def test_get_guild_crest_border_media(self, success_response_mock):
        self.api.wow.game_data.get_guild_crest_border_media(
            "us", "en_US", 0, is_classic=True
        )
        params = {
            "namespace": "static-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/guild-crest/border/0",
            params=params,
        )

    def test_get_guild_crest_emblem_media(self, success_response_mock):
        self.api.wow.game_data.get_guild_crest_emblem_media(
            "us", "en_US", 0, is_classic=True
        )
        params = {
            "namespace": "static-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/guild-crest/emblem/0",
            params=params,
        )

    # Item API

    def test_get_item_classes_index(self, success_response_mock):
        self.api.wow.game_data.get_item_classes_index(
            "us", "en_US", is_classic=True
        )
        params = {
            "namespace": "static-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/item-class/index",
            params=params,
        )

    def test_get_item_class(self, success_response_mock):
        self.api.wow.game_data.get_item_class(
            "us", "en_US", 2, is_classic=True
        )
        params = {
            "namespace": "static-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/item-class/2", params=params
        )

    def test_get_item_sets_index(self, success_response_mock):
        self.api.wow.game_data.get_item_sets_index(
            "us", "en_US", is_classic=True
        )
        params = {
            "namespace": "static-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/item-set/index",
            params=params,
        )

    def test_get_item_set(self, success_response_mock):
        self.api.wow.game_data.get_item_set("us", "en_US", 1, is_classic=True)
        params = {
            "namespace": "static-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/item-set/1", params=params
        )

    def test_get_item_subclass(self, success_response_mock):
        self.api.wow.game_data.get_item_subclass(
            "us", "en_US", 2, 1, is_classic=True
        )
        params = {
            "namespace": "static-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/item-class/2/item-subclass/1",
            params=params,
        )

    def test_get_item(self, success_response_mock):
        self.api.wow.game_data.get_item("us", "en_US", 9999, is_classic=True)
        params = {
            "namespace": "static-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/item/9999", params=params
        )

    def test_get_item_media(self, success_response_mock):
        self.api.wow.game_data.get_item_media(
            "us", "en_US", 9999, is_classic=True
        )
        params = {
            "namespace": "static-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/item/9999",
            params=params,
        )

    # Playable Class API

    def test_get_playable_classes_index(self, success_response_mock):
        self.api.wow.game_data.get_playable_classes_index(
            "us", "en_US", is_classic=True
        )
        params = {
            "namespace": "static-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/playable-class/index",
            params=params,
        )

    def test_get_playable_class(self, success_response_mock):
        self.api.wow.game_data.get_playable_class(
            "us", "en_US", 7, is_classic=True
        )
        params = {
            "namespace": "static-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/playable-class/7",
            params=params,
        )

    def test_get_playable_class_media(self, success_response_mock):
        self.api.wow.game_data.get_playable_class_media(
            "us", "en_US", 7, is_classic=True
        )
        params = {
            "namespace": "static-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/playable-class/7",
            params=params,
        )

    # Playable Race API

    def test_get_playable_races_index(self, success_response_mock):
        self.api.wow.game_data.get_playable_races_index(
            "us", "en_US", is_classic=True
        )
        params = {
            "namespace": "static-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/playable-race/index",
            params=params,
        )

    def test_get_playable_race(self, success_response_mock):
        self.api.wow.game_data.get_playable_race(
            "us", "en_US", 2, is_classic=True
        )
        params = {
            "namespace": "static-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/playable-race/2",
            params=params,
        )

    # Power Type API

    def test_get_power_types_index(self, success_response_mock):
        self.api.wow.game_data.get_power_types_index(
            "us", "en_US", is_classic=True
        )
        params = {
            "namespace": "static-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/power-type/index",
            params=params,
        )

    def test_get_power_type(self, success_response_mock):
        self.api.wow.game_data.get_power_type(
            "us", "en_US", 0, is_classic=True
        )
        params = {
            "namespace": "static-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/power-type/0", params=params
        )

    # Realm API

    def test_get_realms_index(self, success_response_mock):
        self.api.wow.game_data.get_realms_index("us", "en_US", is_classic=True)
        params = {
            "namespace": "dynamic-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/realm/index", params=params
        )

    def test_get_realm(self, success_response_mock):
        self.api.wow.game_data.get_realm(
            "us", "en_US", "tichondrius", is_classic=True
        )
        params = {
            "namespace": "dynamic-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/realm/tichondrius",
            params=params,
        )

    # Region API

    def test_get_regions_index(self, success_response_mock):
        self.api.wow.game_data.get_regions_index(
            "us", "en_US", is_classic=True
        )
        params = {
            "namespace": "dynamic-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/region/index", params=params
        )

    def test_get_region(self, success_response_mock):
        self.api.wow.game_data.get_region("us", "en_US", 1, is_classic=True)
        params = {
            "namespace": "dynamic-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/region/1", params=params
        )

    # Wow Token API

    def test_get_tokens_index(self, success_response_mock):
        self.api.wow.game_data.get_token_index("us", "en_US", is_classic=True)
        params = {
            "namespace": "dynamic-classic-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/token/index", params=params
        )
