from blizzardapi import BlizzardApi


class TestWowProfileApi(object):
    def setup(self):
        self.api = BlizzardApi("client_id", "client_secret")
        self.api.wow.profile._access_token = "access_token"

    # Account Profile API

    def test_get_account_profile_summary(self, success_response_mock):
        self.api.wow.profile.get_account_profile_summary(
            "us", "en_US", "new_access_token"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "new_access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/user/wow", params=params
        )

    def test_get_protected_character_profile_summary(
        self, success_response_mock
    ):
        self.api.wow.profile.get_protected_character_profile_summary(
            "us", "en_US", "new_access_token", 1, 9000
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "new_access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/user/wow/protected-character/1-9000",
            params=params,
        )

    def test_get_account_collections_index(self, success_response_mock):
        self.api.wow.profile.get_account_collections_index(
            "us", "en_US", "new_access_token"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "new_access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/user/wow/collections",
            params=params,
        )

    def test_get_account_mounts_collection_summary(
        self, success_response_mock
    ):
        self.api.wow.profile.get_account_mounts_collection_summary(
            "us", "en_US", "new_access_token"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "new_access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/user/wow/collections/mounts",
            params=params,
        )

    def test_get_account_pets_collection_summary(self, success_response_mock):
        self.api.wow.profile.get_account_pets_collection_summary(
            "us", "en_US", "new_access_token"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "new_access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/user/wow/collections/pets",
            params=params,
        )

    # Character Achievements APIa

    def test_get_character_achievements_summary(self, success_response_mock):
        self.api.wow.profile.get_character_achievements_summary(
            "us", "en_US", "khadgar", "asmon"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/achievements",
            params=params,
        )

    def test_get_character_achievement_statistics(self, success_response_mock):
        self.api.wow.profile.get_character_achievement_statistics(
            "us", "en_US", "moon", "asmon"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/wow/character/moon/asmon/achievements/statistics",
            params=params,
        )

    # Character Appearance API

    def test_get_character_appearance_summary(self, success_response_mock):
        self.api.wow.profile.get_character_appearance_summary(
            "us", "en_US", "khadgar", "asmon"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/appearance",
            params=params,
        )

    # Character Collections API

    def test_get_character_collections_index(self, success_response_mock):
        self.api.wow.profile.get_character_collections_index(
            "us", "en_US", "khadgar", "asmon"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/collections",
            params=params,
        )

    def test_get_character_mounts_collection_index(
        self, success_response_mock
    ):
        self.api.wow.profile.get_character_mounts_collection_index(
            "us", "en_US", "khadgar", "asmon"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/collections/mounts",
            params=params,
        )

    def test_get_character_pets_collection_index(self, success_response_mock):
        self.api.wow.profile.get_character_pets_collection_index(
            "us", "en_US", "khadgar", "asmon"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/collections/pets",
            params=params,
        )

    # Character Encounters API

    def test_get_character_encounters_summary(self, success_response_mock):
        self.api.wow.profile.get_character_encounters_summary(
            "us", "en_US", "khadgar", "asmon"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/encounters",
            params=params,
        )

    def test_get_character_dungeons(self, success_response_mock):
        self.api.wow.profile.get_character_dungeons(
            "us", "en_US", "khadgar", "asmon"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/encounters/dungeons",
            params=params,
        )

    def test_get_character_raids(self, success_response_mock):
        self.api.wow.profile.get_character_raids(
            "us", "en_US", "khadgar", "asmon"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/encounters/raids",
            params=params,
        )

    # Character Equipment API

    def test_get_character_equipment_summary(self, success_response_mock):
        self.api.wow.profile.get_character_equipment_summary(
            "us", "en_US", "khadgar", "asmon"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/equipment",
            params=params,
        )

    # Character Hunter Pets API

    def test_get_character_hunter_pets_summary(self, success_response_mock):
        self.api.wow.profile.get_character_hunter_pets_summary(
            "us", "en_US", "khadgar", "asmon"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/hunter-pets",
            params=params,
        )

    # Character Media API

    def test_get_character_media_summary(self, success_response_mock):
        self.api.wow.profile.get_character_media_summary(
            "us", "en_US", "khadgar", "asmon"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/character-media",
            params=params,
        )

    # Character Mythic Keystone Profile API

    def test_get_character_mythic_keystone_profile_index(
        self, success_response_mock
    ):
        self.api.wow.profile.get_character_mythic_keystone_profile_index(
            "us", "en_US", "blackmoore", "ayanda"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "{0}/profile/wow/character/blackmoore/ayanda/mythic-keystone-profile".format(
                "https://us.api.blizzard.com"
            ),
            params=params,
        )

    def test_get_character_mythic_keystone_profile_season_details(
        self, success_response_mock
    ):
        self.api.wow.profile.get_character_mythic_keystone_profile_season_details(
            "us", "en_US", "blackmoore", "ayanda", 1
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "{0}/profile/wow/character/blackmoore/ayanda/mythic-keystone-profile/season/1".format(
                "https://us.api.blizzard.com"
            ),
            params=params,
        )

    # Character Professions API

    def test_get_character_professions_summary(self, success_response_mock):
        self.api.wow.profile.get_character_professions_summary(
            "us", "en_US", "khadgar", "asmon"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/professions",
            params=params,
        )

    # Character Profile API

    def test_get_character_profile_summary(self, success_response_mock):
        self.api.wow.profile.get_character_profile_summary(
            "us", "en_US", "khadgar", "asmon"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/wow/character/khadgar/asmon",
            params=params,
        )

    def test_get_character_profile_status(self, success_response_mock):
        self.api.wow.profile.get_character_profile_status(
            "us", "en_US", "khadgar", "asmon"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/status",
            params=params,
        )

    # Character PvP API

    def test_get_character_pvp_bracket_statistics(self, success_response_mock):
        self.api.wow.profile.get_character_pvp_bracket_statistics(
            "us", "en_US", "khadgar", "asmon", "3v3"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/pvp-bracket/3v3",
            params=params,
        )

    def test_get_character_pvp_summary(self, success_response_mock):
        self.api.wow.profile.get_character_pvp_summary(
            "us", "en_US", "khadgar", "asmon"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/pvp-summary",
            params=params,
        )

    # Character Quests API

    def test_get_character_quests(self, success_response_mock):
        self.api.wow.profile.get_character_quests(
            "us", "en_US", "khadgar", "asmon"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/quests",
            params=params,
        )

    def test_get_character_completed_quests(self, success_response_mock):
        self.api.wow.profile.get_character_completed_quests(
            "us", "en_US", "khadgar", "asmon"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/quests/completed",
            params=params,
        )

    # Character Reputations API

    def test_get_character_reputations_summary(self, success_response_mock):
        self.api.wow.profile.get_character_reputations_summary(
            "us", "en_US", "khadgar", "asmon"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/reputations",
            params=params,
        )

    # Character Specializations API

    def test_get_character_specializations_summary(
        self, success_response_mock
    ):
        self.api.wow.profile.get_character_specializations_summary(
            "us", "en_US", "khadgar", "asmon"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/specializations",
            params=params,
        )

    # Character Statistics API

    def test_get_character_statistics_summary(self, success_response_mock):
        self.api.wow.profile.get_character_statistics_summary(
            "us", "en_US", "khadgar", "asmon"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/statistics",
            params=params,
        )

    # Character Titles API

    def test_get_character_titles_summary(self, success_response_mock):
        self.api.wow.profile.get_character_titles_summary(
            "us", "en_US", "khadgar", "asmon"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/profile/wow/character/khadgar/asmon/titles",
            params=params,
        )

    # Guild API

    def test_get_guild(self, success_response_mock):
        self.api.wow.profile.get_guild("us", "en_US", "khadgar", "bestguild")
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/guild/khadgar/bestguild",
            params=params,
        )

    def test_get_guild_activity(self, success_response_mock):
        self.api.wow.profile.get_guild_activity(
            "us", "en_US", "khadgar", "bestguild"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/guild/khadgar/bestguild/activity",
            params=params,
        )

    def test_get_guild_achievements(self, success_response_mock):
        self.api.wow.profile.get_guild_achievements(
            "us", "en_US", "khadgar", "bestguild"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/guild/khadgar/bestguild/achievements",
            params=params,
        )

    def test_get_guild_roster(self, success_response_mock):
        self.api.wow.profile.get_guild_roster(
            "us", "en_US", "khadgar", "bestguild"
        )
        params = {
            "namespace": "profile-us",
            "locale": "en_US",
            "access_token": "access_token",
        }
        success_response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/guild/khadgar/bestguild/roster",
            params=params,
        )
