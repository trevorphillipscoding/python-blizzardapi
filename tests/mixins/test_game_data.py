from blizzardapi import BlizzardApi


class TestGameDataMixin:
    def setup(self):
        self.api = BlizzardApi("client-id", "client-secret", "access_token")

        self.params = {
            "access_token": "access_token",
            "locale": "en_US",
        }

    # Achievement API

    def test_get_achievement_categories_index(self, response_mock):
        self.api.get_achievement_categories_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/achievement-category/index",
            params=params,
        )

    def test_get_achievement_category(self, response_mock):
        self.api.get_achievement_category(81)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/achievement-category/81",
            params=params,
        )

    def test_get_achievements_index(self, response_mock):
        self.api.get_achievements_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/achievement/index", params=params
        )

    def test_get_achievement(self, response_mock):
        self.api.get_achievement(6)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/achievement/6", params=params
        )

    def test_get_achievement_media(self, response_mock):
        self.api.get_achievement_media(6)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/achievement/6", params=params
        )

    # Auction House API

    def test_get_auctions(self, response_mock):
        self.api.get_auctions(1146)
        params = self.params
        params["namespace"] = "dynamic-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/connected-realm/1146/auctions",
            params=params,
        )

    # Azerite Essence API

    def test_get_azerite_essences_index(self, response_mock):
        self.api.get_azerite_essences_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/azerite-essence/index", params=params
        )

    def test_get_azerite_essence(self, response_mock):
        self.api.get_azerite_essence(2)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/azerite-essence/2", params=params
        )

    def test_get_azerite_essence_media(self, response_mock):
        self.api.get_azerite_essence_media(2)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/azerite-essence/2",
            params=params,
        )

    # Connected Realm API

    def test_get_connected_realms_index(self, response_mock):
        self.api.get_connected_realms_index()
        params = self.params
        params["namespace"] = "dynamic-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/connected-realm/index", params=params
        )

    def test_get_connected_realm(self, response_mock):
        self.api.get_connected_realm(1)
        params = self.params
        params["namespace"] = "dynamic-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/connected-realm/1", params=params
        )

    # Creature API

    def test_get_creature_families_index(self, response_mock):
        self.api.get_creature_families_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/creature-family/index", params=params
        )

    def test_get_creature_family(self, response_mock):
        self.api.get_creature_family(1)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/creature-family/1", params=params
        )

    def test_get_creature_types_index(self, response_mock):
        self.api.get_creature_types_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/creature-type/index", params=params
        )

    def test_get_creature_type(self, response_mock):
        self.api.get_creature_type(1)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/creature-type/1", params=params
        )

    def test_get_creature(self, response_mock):
        self.api.get_creature(1)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/creature/1", params=params
        )

    def test_get_creature_display_media(self, response_mock):
        self.api.get_creature_display_media(1)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/creature-display/1",
            params=params,
        )

    def test_get_creature_family_media(self, response_mock):
        self.api.get_creature_family_media(1)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/creature-family/1",
            params=params,
        )

    # Guild Crest API

    def test_get_guild_crest_components_index(self, response_mock):
        self.api.get_guild_crest_components_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/guild-crest/index", params=params
        )

    def test_get_guild_crest_border_media(self, response_mock):
        self.api.get_guild_crest_border_media(0)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/guild-crest/border/0",
            params=params,
        )

    def test_get_guild_crest_emblem_media(self, response_mock):
        self.api.get_guild_crest_emblem_media(0)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/guild-crest/emblem/0",
            params=params,
        )

    # Item API

    def test_get_item_classes_index(self, response_mock):
        self.api.get_item_classes_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/item-class/index", params=params
        )

    def test_get_item_class(self, response_mock):
        self.api.get_item_class(2)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/item-class/2", params=params
        )

    def test_get_item_sets_index(self, response_mock):
        self.api.get_item_sets_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/item-set/index", params=params
        )

    def test_get_item_set(self, response_mock):
        self.api.get_item_set(1)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/item-set/1", params=params
        )

    def test_get_item_subclass(self, response_mock):
        self.api.get_item_subclass(2, 1)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/item-class/2/item-subclass/1",
            params=params,
        )

    def test_get_item(self, response_mock):
        self.api.get_item(9999)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/item/9999", params=params
        )

    def test_get_item_media(self, response_mock):
        self.api.get_item_media(9999)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/item/9999", params=params
        )

    # Journal API

    def test_get_journal_expansions_index(self, response_mock):
        self.api.get_journal_expansions_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/journal-expansion/index",
            params=params,
        )

    def test_get_journal_expansion(self, response_mock):
        self.api.get_journal_expansion(68)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/journal-expansion/68", params=params
        )

    def test_get_journal_encounters_index(self, response_mock):
        self.api.get_journal_encounters_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/journal-encounter/index",
            params=params,
        )

    def test_get_journal_encounter(self, response_mock):
        self.api.get_journal_encounter(89)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/journal-encounter/89", params=params
        )

    def test_get_journal_instances_index(self, response_mock):
        self.api.get_journal_instances_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/journal-instance/index", params=params
        )

    def test_get_journal_instance(self, response_mock):
        self.api.get_journal_instance(63)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/journal-instance/63", params=params
        )

    def test_get_journal_instance_media(self, response_mock):
        self.api.get_journal_instance_media(63)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/journal-instance/63",
            params=params,
        )

    # Modified Crafting API

    def test_get_modified_crafting_index(self, response_mock):
        self.api.get_modified_crafting_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/modified-crafting/index",
            params=params,
        )

    def test_get_modified_crafting_category_index(self, response_mock):
        self.api.get_modified_crafting_category_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/modified-crafting/category/index",
            params=params,
        )

    def test_get_modified_crafting_category(self, response_mock):
        self.api.get_modified_crafting_category(1)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/modified-crafting/category/1",
            params=params,
        )

    def test_get_modified_crafting_reagent_slot_type_index(self, response_mock):
        self.api.get_modified_crafting_reagent_slot_type_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/modified-crafting/reagent-slot-type/index",
            params=params,
        )

    def test_get_modified_crafting_reagent_slot_type(self, response_mock):
        self.api.get_modified_crafting_reagent_slot_type(16)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/modified-crafting/reagent-slot-type/16",
            params=params,
        )

    # Mount API

    def test_get_mounts_index(self, response_mock):
        self.api.get_mounts_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/mount/index", params=params
        )

    def test_get_mount(self, response_mock):
        self.api.get_mount(6)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/mount/6", params=params
        )

    # Mythic Keystone Affix API

    def test_get_mythic_keystone_affixes_index(self, response_mock):
        self.api.get_mythic_keystone_affixes_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/keystone-affix/index", params=params
        )

    def test_get_mythic_keystone_affix(self, response_mock):
        self.api.get_mythic_keystone_affix(3)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/keystone-affix/3", params=params
        )

    def test_get_mythic_keystone_affix_media(self, response_mock):
        self.api.get_mythic_keystone_affix_media(1)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/keystone-affix/1", params=params
        )

    # Mythic Keystone Dungeon API

    def test_get_mythic_keystone_dungeons_index(self, response_mock):
        self.api.get_mythic_keystone_dungeons_index()
        params = self.params
        params["namespace"] = "dynamic-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/mythic-keystone/dungeon/index",
            params=params,
        )

    def test_get_mythic_keystone_dungeon(self, response_mock):
        self.api.get_mythic_keystone_dungeon(5)
        params = self.params
        params["namespace"] = "dynamic-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/mythic-keystone/dungeon/5",
            params=params,
        )

    def test_get_mythic_keystone_index(self, response_mock):
        self.api.get_mythic_keystone_index()
        params = self.params
        params["namespace"] = "dynamic-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/mythic-keystone/index", params=params
        )

    def test_get_mythic_keystone_periods_index(self, response_mock):
        self.api.get_mythic_keystone_periods_index()
        params = self.params
        params["namespace"] = "dynamic-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/mythic-keystone/period/index",
            params=params,
        )

    def test_get_mythic_keystone_period(self, response_mock):
        self.api.get_mythic_keystone_period(641)
        params = self.params
        params["namespace"] = "dynamic-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/mythic-keystone/period/641",
            params=params,
        )

    def test_get_mythic_keystone_seasons_index(self, response_mock):
        self.api.get_mythic_keystone_seasons_index()
        params = self.params
        params["namespace"] = "dynamic-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/mythic-keystone/season/index",
            params=params,
        )

    def test_get_mythic_keystone_season(self, response_mock):
        self.api.get_mythic_keystone_season(1)
        params = self.params
        params["namespace"] = "dynamic-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/mythic-keystone/season/1",
            params=params,
        )

    # Mythic Keystone Leaderboard API

    def test_get_mythic_keystone_leaderboards_index(self, response_mock):
        self.api.get_mythic_keystone_leaderboards_index(1)
        params = self.params
        params["namespace"] = "dynamic-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/connected-realm/1/mythic-leaderboard/index",
            params=params,
        )

    def test_get_mythic_keystone_leaderboard(self, response_mock):
        self.api.get_mythic_keystone_leaderboard(1, 2, 3)
        params = self.params
        params["namespace"] = "dynamic-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/connected-realm/1/mythic-leaderboard/2/period/3",
            params=params,
        )

    # Mythic Raid Leaderboard API

    def test_get_mythic_raid_leaderboard(self, response_mock):
        self.api.get_mythic_raid_leaderboard("uldir", "horde")
        params = self.params
        params["namespace"] = "dynamic-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/leaderboard/hall-of-fame/uldir/horde",
            params=params,
        )

    # Pet API

    def test_get_pets_index(self, response_mock):
        self.api.get_pets_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pet/index", params=params
        )

    def test_get_pet(self, response_mock):
        self.api.get_pet(39)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pet/39", params=params
        )

    def test_get_pet_media(self, response_mock):
        self.api.get_pet_media(39)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/pet/39", params=params
        )

    def test_get_pet_abilities_index(self, response_mock):
        self.api.get_pet_abilities_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pet-ability/index", params=params
        )

    def test_get_pet_ability(self, response_mock):
        self.api.get_pet_ability(110)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pet-ability/110", params=params
        )

    def test_get_pet_ability_media(self, response_mock):
        self.api.get_pet_ability_media(110)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/pet-ability/110", params=params
        )

    # Playable Class API

    def test_get_playable_classes_index(self, response_mock):
        self.api.get_playable_classes_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/playable-class/index", params=params
        )

    def test_get_playable_class(self, response_mock):
        self.api.get_playable_class(7)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/playable-class/7", params=params
        )

    def test_get_playable_class_media(self, response_mock):
        self.api.get_playable_class_media(7)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/playable-class/7", params=params
        )

    def test_get_pvp_talent_slots(self, response_mock):
        self.api.get_pvp_talent_slots(7)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/playable-class/7/pvp-talent-slots",
            params=params,
        )

    # Playable Race API

    def test_get_playable_races_index(self, response_mock):
        self.api.get_playable_races_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/playable-race/index", params=params
        )

    def test_get_playable_race(self, response_mock):
        self.api.get_playable_race(2)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/playable-race/2", params=params
        )

    # Playable Specialization API

    def test_get_playable_specializations_index(self, response_mock):
        self.api.get_playable_specializations_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/playable-specialization/index",
            params=params,
        )

    def test_get_playable_specialization(self, response_mock):
        self.api.get_playable_specialization(262)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/playable-specialization/262",
            params=params,
        )

    def test_get_playable_specialization_media(self, response_mock):
        self.api.get_playable_specialization_media(262)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/playable-specialization/262",
            params=params,
        )

    # Power Type API

    def test_get_power_types_index(self, response_mock):
        self.api.get_power_types_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/power-type/index", params=params
        )

    def test_get_power_type(self, response_mock):
        self.api.get_power_type(0)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/power-type/0", params=params
        )

    # Profession API

    def test_get_professions_index(self, response_mock):
        self.api.get_professions_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/profession/index", params=params
        )

    def test_get_profession(self, response_mock):
        self.api.get_profession(164)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/profession/164", params=params
        )

    def test_get_profession_media(self, response_mock):
        self.api.get_profession_media(164)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/profession/164", params=params
        )

    def test_get_profession_skill_tier(self, response_mock):
        self.api.get_profession_skill_tier(164, 2477)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/profession/164/skill-tier/2477",
            params=params,
        )

    def test_get_recipe(self, response_mock):
        self.api.get_recipe(1631)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/recipe/1631", params=params
        )

    def test_get_recipe_media(self, response_mock):
        self.api.get_recipe_media(1631)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/recipe/1631", params=params
        )

    # PvP Season API

    def test_get_pvp_seasons_index(self, response_mock):
        self.api.get_pvp_seasons_index()
        params = self.params
        params["namespace"] = "dynamic-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pvp-season/index", params=params
        )

    def test_get_pvp_season(self, response_mock):
        self.api.get_pvp_season(27)
        params = self.params
        params["namespace"] = "dynamic-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pvp-season/27", params=params
        )

    def test_get_pvp_leaderboards_index(self, response_mock):
        self.api.get_pvp_leaderboards_index(27)
        params = self.params
        params["namespace"] = "dynamic-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pvp-season/27/pvp-leaderboard/index",
            params=params,
        )

    def test_get_pvp_leaderboard(self, response_mock):
        self.api.get_pvp_leaderboard(27, "3v3")
        params = self.params
        params["namespace"] = "dynamic-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pvp-season/27/pvp-leaderboard/3v3",
            params=params,
        )

    def test_get_pvp_rewards_index(self, response_mock):
        self.api.get_pvp_rewards_index(27)
        params = self.params
        params["namespace"] = "dynamic-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pvp-season/27/pvp-reward/index",
            params=params,
        )

    # PvP Tier API

    def test_get_pvp_tier_media(self, response_mock):
        self.api.get_pvp_tier_media(1)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/pvp-tier/1", params=params
        )

    def test_get_pvp_tiers_index(self, response_mock):
        self.api.get_pvp_tiers_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pvp-tier/index", params=params
        )

    def test_get_pvp_tier(self, response_mock):
        self.api.get_pvp_tier(1)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pvp-tier/1", params=params
        )

    # Quest API

    def test_get_quests_index(self, response_mock):
        self.api.get_quests_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/quest/index", params=params
        )

    def test_get_quest(self, response_mock):
        self.api.get_quest(2)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/quest/2", params=params
        )

    def test_get_quest_categories_index(self, response_mock):
        self.api.get_quest_categories_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/quest/category/index", params=params
        )

    def test_get_quest_category(self, response_mock):
        self.api.get_quest_category(1)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/quest/category/1", params=params
        )

    def test_get_quest_areas_index(self, response_mock):
        self.api.get_quest_areas_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/quest/area/index", params=params
        )

    def test_get_quest_area(self, response_mock):
        self.api.get_quest_area(1)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/quest/area/1", params=params
        )

    def test_get_quest_types_index(self, response_mock):
        self.api.get_quest_types_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/quest/type/index", params=params
        )

    def test_get_quest_type(self, response_mock):
        self.api.get_quest_type(1)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/quest/type/1", params=params
        )

    # Realm API

    def test_get_realms_index(self, response_mock):
        self.api.get_realms_index()
        params = self.params
        params["namespace"] = "dynamic-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/realm/index", params=params
        )

    def test_get_realm(self, response_mock):
        self.api.get_realm("tichondrius")
        params = self.params
        params["namespace"] = "dynamic-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/realm/tichondrius", params=params
        )

    # Region API

    def test_get_regions_index(self, response_mock):
        self.api.get_regions_index()
        params = self.params
        params["namespace"] = "dynamic-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/region/index", params=params
        )

    def test_get_region(self, response_mock):
        self.api.get_region(1)
        params = self.params
        params["namespace"] = "dynamic-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/region/1", params=params
        )

    # Reputations API

    def test_get_reputation_factions_index(self, response_mock):
        self.api.get_reputation_factions_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/reputation-faction/index",
            params=params,
        )

    def test_get_reputation_faction(self, response_mock):
        self.api.get_reputation_faction(21)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/reputation-faction/21", params=params
        )

    def test_get_reputation_tiers_index(self, response_mock):
        self.api.get_reputation_tiers_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/reputation-tiers/index", params=params
        )

    def test_get_reputation_tier(self, response_mock):
        self.api.get_reputation_tier(2)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/reputation-tiers/2", params=params
        )

    # Spell API

    def test_get_spell(self, response_mock):
        self.api.get_spell(196607)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/spell/196607", params=params
        )

    def test_get_spell_media(self, response_mock):
        self.api.get_spell_media(196607)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/media/spell/196607", params=params
        )

    # Talent API

    def test_get_talents_index(self, response_mock):
        self.api.get_talents_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/talent/index", params=params
        )

    def test_get_talent(self, response_mock):
        self.api.get_talent(23106)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/talent/23106", params=params
        )

    def test_get_pvp_talents_index(self, response_mock):
        self.api.get_pvp_talents_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pvp-talent/index", params=params
        )

    def test_get_pvp_talent(self, response_mock):
        self.api.get_pvp_talent(3)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/pvp-talent/3", params=params
        )

    # Title API

    def test_get_titles_index(self, response_mock):
        self.api.get_titles_index()
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/title/index", params=params
        )

    def test_get_title(self, response_mock):
        self.api.get_title(1)
        params = self.params
        params["namespace"] = "static-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/title/1", params=params
        )

    # WoW Token API

    def test_get_tokens_index(self, response_mock):
        self.api.get_token_index()
        params = self.params
        params["namespace"] = "dynamic-us"
        response_mock.assert_called_with(
            "https://us.api.blizzard.com/data/wow/token/index", params=params
        )
