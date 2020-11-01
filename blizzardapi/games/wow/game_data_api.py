from ..api import Api


class GameDataApi(Api):
    """All Game Data API methods"""

    def __init__(self, access_token, region, locale):
        super().__init__(access_token, region)
        self._locale = locale

    # Achievement API

    def get_achievement_categories_index(self):
        """
        Achievement API - Returns an index of achievement categories.
        """
        resource = f"/data/wow/achievement-category/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_achievement_category(self, achievement_category_id):
        """
        Achievement API - Returns an achievement category by ID.
        """
        resource = f"/data/wow/achievement-category/{achievement_category_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_achievements_index(self):
        """
        Achievement API - Returns an index of achievements.
        """
        resource = f"/data/wow/achievement/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_achievement(self, achievement_id):
        """
        Achievement API - Returns an achievement by ID.
        """
        resource = f"/data/wow/achievement/{achievement_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_achievement_media(self, achievement_id):
        """
        Achievement API - Returns media for an achievement by ID.
        """
        resource = f"/data/wow/media/achievement/{achievement_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Auction House API

    def get_auctions(self, connected_realm_id):
        """
        Auction House API - Returns all active auctions for a connected realm.
        """
        resource = f"/data/wow/connected-realm/{connected_realm_id}/auctions"
        namespace = f"dynamic-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Azerite Essence API

    def get_azerite_essences_index(self):
        """
        Azerite Essence API - Returns an index of azerite essences.
        """
        resource = f"/data/wow/azerite-essence/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_azerite_essence(self, azerite_essence_id):
        """
        Azerite Essence API - Returns an azerite essence by ID.
        """
        resource = f"/data/wow/azerite-essence/{azerite_essence_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_azerite_essence_media(self, azerite_essence_id):
        """
        Azerite Essence API - Returns media for an azerite essence by ID.
        """
        resource = f"/data/wow/media/azerite-essence/{azerite_essence_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Connected Realm API

    def get_connected_realms_index(self):
        """
        Connected Realm API - Returns an index of connected realms.
        """
        resource = f"/data/wow/connected-realm/index"
        namespace = f"dynamic-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_connected_realm(self, connected_realm_id):
        """
        Connected Realm API - Returns a connected realm by ID.
        """
        resource = f"/data/wow/connected-realm/{connected_realm_id}"
        namespace = f"dynamic-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Creature API

    def get_creature_families_index(self):
        """
        Creature API - Returns an index of creature families.
        """
        resource = f"/data/wow/creature-family/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_creature_family(self, creature_family_id):
        """
        Creature API - Returns a creature family by ID.
        """
        resource = f"/data/wow/creature-family/{creature_family_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_creature_types_index(self):
        """
        Creature API - Returns an index of creature types.
        """
        resource = f"/data/wow/creature-type/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_creature_type(self, creature_type_id):
        """
        Creature API - Returns a creature type by ID.
        """
        resource = f"/data/wow/creature-type/{creature_type_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_creature(self, creature_id):
        """
        Creature API - Returns a creature by ID.
        """
        resource = f"/data/wow/creature/{creature_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_creature_display_media(self, creature_display_id):
        """
        Creature API - Returns media for a creature display by ID.
        """
        resource = f"/data/wow/media/creature-display/{creature_display_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_creature_family_media(self, creature_family_id):
        """
        Creature API - Returns media for a creature family by ID.
        """
        resource = f"/data/wow/media/creature-family/{creature_family_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Guild Crest API

    def get_guild_crest_components_index(self):
        """
        Guild Crest API - Returns an index of guild crest media.
        """
        resource = f"/data/wow/guild-crest/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_guild_crest_border_media(self, border_id):
        """
        Guild Crest API - Returns media for a guild crest border by ID.
        """
        resource = f"/data/wow/media/guild-crest/border/{border_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_guild_crest_emblem_media(self, emblem_id):
        """
        Guild Crest API - Returns media for a guild crest emblem by ID.
        """
        resource = f"/data/wow/media/guild-crest/emblem/{emblem_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Item API

    def get_item_classes_index(self):
        """
        Item API - Returns an index of item classes.
        """
        resource = f"/data/wow/item-class/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_item_class(self, item_class_id):
        """
        Item API - Returns an item class by ID.
        """
        resource = f"/data/wow/item-class/{item_class_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_item_sets_index(self):
        """
        Item API - Returns an index of item sets.
        """
        resource = f"/data/wow/item-set/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_item_set(self, item_set_id):
        """
        Item API - Returns an item set by ID.
        """
        resource = f"/data/wow/item-set/{item_set_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_item_subclass(self, item_class_id, item_subclass_id):
        """
        Item API - Returns an item subclass by ID.
        """
        resource = f"/data/wow/item-class/{item_class_id}/item-subclass/{item_subclass_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_item(self, item_id):
        """
        Item API - Returns an item by ID.
        """
        resource = f"/data/wow/item/{item_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_item_media(self, item_id):
        """
        Item API - Returns media for an item by ID.
        """
        resource = f"/data/wow/media/item/{item_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Journal API

    def get_journal_expansions_index(self):
        """
        Journal API - Returns an index of journal expansions.
        """
        resource = f"/data/wow/journal-expansion/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_journal_expansion(self, journal_expansion_id):
        """
        Journal API - Returns a journal expansion by ID.
        """
        resource = f"/data/wow/journal-expansion/{journal_expansion_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_journal_encounters_index(self):
        """
        Journal API - Returns an index of journal encounters.
        """
        resource = f"/data/wow/journal-encounter/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_journal_encounter(self, journal_encounter_id):
        """
        Journal API - Returns a journal encounter by ID.
        """
        resource = f"/data/wow/journal-encounter/{journal_encounter_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_journal_instances_index(self):
        """
        Journal API - Returns an index of journal instances.
        """
        resource = f"/data/wow/journal-instance/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_journal_instance(self, journal_instance_id):
        """
        Journal API - Returns a journal instance.
        """
        resource = f"/data/wow/journal-instance/{journal_instance_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_journal_instance_media(self, journal_instance_id):
        """
        Journal API - Returns media for a journal instance by ID.
        """
        resource = f"/data/wow/media/journal-instance/{journal_instance_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Modified Crafting API

    def get_modified_crafting_index(self):
        """
        Modified Crafting API - Returns the parent index for Modified Crafting.
        """
        resource = f"/data/wow/modified-crafting/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_modified_crafting_category_index(self):
        """
        Modified Crafting API - Returns the index of Modified Crafting categories.
        """
        resource = f"/data/wow/modified-crafting/category/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_modified_crafting_category(self, category_id):
        """
        Modified Crafting API - Returns the index of Modified Crafting categories.
        """
        resource = f"/data/wow/modified-crafting/category/{category_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_modified_crafting_reagent_slot_type_index(self):
        """
        Modified Crafting API - Returns the index of Modified Crafting reagent slot types.
        """
        resource = f"/data/wow/modified-crafting/reagent-slot-type/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_modified_crafting_reagent_slot_type(self, slot_type_id):
        """
        Modified Crafting API - Returns a Modified Crafting reagent slot type by ID.
        """
        resource = f"/data/wow/modified-crafting/reagent-slot-type/{slot_type_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Mount API

    def get_mounts_index(self):
        """
        Mount API - Returns an index of mounts.
        """
        resource = f"/data/wow/mount/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_mount(self, mount_id):
        """
        Mount API - Returns a mount by ID.
        """
        resource = f"/data/wow/mount/{mount_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Mythic Keystone Affix API

    def get_mythic_keystone_affixes_index(self):
        """
        Mythic Keystone Affix API - Returns an index of mythic keystone affixes.
        """
        resource = f"/data/wow/keystone-affix/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_mythic_keystone_affix(self, keystone_affix_id):
        """
        Mythic Keystone Affix API - Returns a mythic keystone affix by ID.
        """
        resource = f"/data/wow/keystone-affix/{keystone_affix_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_mythic_keystone_affix_media(self, keystone_affix_id):
        """
        Mythic Keystone Affix API - Returns media for a mythic keystone affix by ID.
        """
        resource = f"/data/wow/media/keystone-affix/{keystone_affix_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Mythic Keystone Dungeon API

    def get_mythic_keystone_dungeons_index(self):
        """
        Mythic Keystone Dungeon API - Returns an index of Mythic Keystone dungeons.
        """
        resource = f"/data/wow/mythic-keystone/dungeon/index"
        namespace = f"dynamic-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_mythic_keystone_dungeon(self, dungeon_id):
        """
        Mythic Keystone Dungeon API - Returns a Mythic Keystone dungeon by ID.
        """
        resource = f"/data/wow/mythic-keystone/dungeon/{dungeon_id}"
        namespace = f"dynamic-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_mythic_keystone_index(self):
        """
        Mythic Keystone Dungeon API - Returns an index of links to other documents related to
        Mythic Keystone dungeons.
        """
        resource = f"/data/wow/mythic-keystone/index"
        namespace = f"dynamic-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_mythic_keystone_periods_index(self):
        """
        Mythic Keystone Dungeon API - Returns an index of Mythic Keystone periods.
        """
        resource = f"/data/wow/mythic-keystone/period/index"
        namespace = f"dynamic-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_mythic_keystone_period(self, period_id):
        """
        Mythic Keystone Dungeon API - Returns a Mythic Keystone period by ID.
        """
        resource = f"/data/wow/mythic-keystone/period/{period_id}"
        namespace = f"dynamic-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_mythic_keystone_seasons_index(self):
        """
        Mythic Keystone Dungeon API - Returns an index of Mythic Keystone seasons.
        """
        resource = f"/data/wow/mythic-keystone/season/index"
        namespace = f"dynamic-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_mythic_keystone_season(self, season_id):
        """
        Mythic Keystone Dungeon API - Returns a Mythic Keystone season by ID.
        """
        resource = f"/data/wow/mythic-keystone/season/{season_id}"
        namespace = f"dynamic-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Mythic Keystone Leaderboard API

    def get_mythic_keystone_leaderboards_index(self, connected_realm_id):
        """
        Mythic Keystone Leaderboard API - Returns an index of Mythic Keystone Leaderboard dungeon
        instances for a connected realm.
        """
        resource = f"/data/wow/connected-realm/{connected_realm_id}/mythic-leaderboard/index"
        namespace = f"dynamic-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_mythic_keystone_leaderboard(
        self, connected_realm_id, dungeon_id, period_id
    ):
        """
        Mythic Keystone Leaderboard API - Returns a weekly Mythic Keystone Leaderboard by period.
        """
        resource = f"/data/wow/connected-realm/{connected_realm_id}/mythic-leaderboard/{dungeon_id}/period/{period_id}"
        namespace = f"dynamic-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Mythic Raid Leaderboard API

    def get_mythic_raid_leaderboard(self, raid, faction):
        """
        Mythic Raid Leaderboard API - Returns the leaderboard for a given raid and faction.
        """
        resource = f"/data/wow/leaderboard/hall-of-fame/{raid}/{faction}"
        namespace = f"dynamic-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Pet API

    def get_pets_index(self):
        """
        Pet API - Returns an index of battle pets.
        """
        resource = f"/data/wow/pet/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_pet(self, pet_id):
        """
        Pet API - Returns a battle pets by ID.
        """
        resource = f"/data/wow/pet/{pet_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_pet_media(self, pet_id):
        """
        Pet API - Returns media for a battle pet by ID.
        """
        resource = f"/data/wow/media/pet/{pet_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_pet_abilities_index(self):
        """
        Pet API - Returns an index of pet abilities.
        """
        resource = f"/data/wow/pet-ability/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_pet_ability(self, pet_ability_id):
        """
        Pet API - Returns a pet ability by ID.
        """
        resource = f"/data/wow/pet-ability/{pet_ability_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_pet_ability_media(self, pet_ability_id):
        """
        Pet API - Returns media for a pet ability by ID.
        """
        resource = f"/data/wow/media/pet-ability/{pet_ability_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Playable Class API

    def get_playable_classes_index(self):
        """
        Playable Class API - Returns an index of playable classes.
        """
        resource = f"/data/wow/playable-class/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_playable_class(self, class_id):
        """
        Playable Class API - Returns a playable class by ID.
        """
        resource = f"/data/wow/playable-class/{class_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_playable_class_media(self, playable_class_id):
        """
        Playable Class API - Returns media for a playable class by ID.
        """
        resource = f"/data/wow/media/playable-class/{playable_class_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_pvp_talent_slots(self, class_id):
        """
        Playable Class API - Returns the PvP talent slots for a playable class by ID.
        """
        resource = f"/data/wow/playable-class/{class_id}/pvp-talent-slots"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Playable Race API

    def get_playable_races_index(self):
        """
        Playable Race API - Returns an index of playable races.
        """
        resource = f"/data/wow/playable-race/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_playable_race(self, playable_race_id):
        """
        Playable Race API - Returns a playable race by ID.
        """
        resource = f"/data/wow/playable-race/{playable_race_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Playable Specialization API

    def get_playable_specializations_index(self):
        """
        Playable Specialization API - Returns an index of playable specializations.
        """
        resource = f"/data/wow/playable-specialization/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_playable_specialization(self, spec_id):
        """
        Playable Specialization API - Returns a playable specialization by ID.
        """
        resource = f"/data/wow/playable-specialization/{spec_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_playable_specialization_media(self, spec_id):
        """
        Playable Specialization API - Returns media for a playable specialization by ID.
        """
        resource = f"/data/wow/media/playable-specialization/{spec_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Power Type API

    def get_power_types_index(self):
        """
        Power Type API - Returns an index of power types.
        """
        resource = f"/data/wow/power-type/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_power_type(self, power_type_id):
        """
        Power Type API - Returns a power type by ID.
        """
        resource = f"/data/wow/power-type/{power_type_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Profession API

    def get_professions_index(self):
        """
        Profession API - Returns an index of professions.
        """
        resource = f"/data/wow/profession/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_profession(self, profession_id):
        """
        Profession API - Returns a profession by ID.
        """
        resource = f"/data/wow/profession/{profession_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_profession_media(self, profession_id):
        """
        Profession API - Returns media for a profession by ID.
        """
        resource = f"/data/wow/media/profession/{profession_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_profession_skill_tier(self, profession_id, skill_tier_id):
        """
        Profession API - Returns a skill tier for a profession by ID.
        """
        resource = f"/data/wow/profession/{profession_id}/skill-tier/{skill_tier_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_recipe(self, recipe_id):
        """
        Profession API - Returns a recipe by ID.
        """
        resource = f"/data/wow/recipe/{recipe_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_recipe_media(self, recipe_id):
        """
        Profession API - Returns media for a recipe by ID.
        """
        resource = f"/data/wow/media/recipe/{recipe_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # PvP Season API

    def get_pvp_seasons_index(self):
        """
        PvP Season API - Returns an index of PvP seasons.
        """
        resource = f"/data/wow/pvp-season/index"
        namespace = f"dynamic-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_pvp_season(self, pvp_season_id):
        """
        PvP Season API - Returns a PvP season by ID.
        """
        resource = f"/data/wow/pvp-season/{pvp_season_id}"
        namespace = f"dynamic-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_pvp_leaderboards_index(self, pvp_season_id):
        """
        PvP Season API - Returns an index of PvP leaderboards for a PvP season.
        """
        resource = f"/data/wow/pvp-season/{pvp_season_id}/pvp-leaderboard/index"
        namespace = f"dynamic-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_pvp_leaderboard(self, pvp_season_id, pvp_bracket):
        """
        PvP Season API - Returns the PvP leaderboard of a specific PvP bracket for a PvP season.
        """
        resource = f"/data/wow/pvp-season/{pvp_season_id}/pvp-leaderboard/{pvp_bracket}"
        namespace = f"dynamic-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_pvp_rewards_index(self, pvp_season_id):
        """
        PvP Season API - Returns an index of PvP rewards for a PvP season.
        """
        resource = f"/data/wow/pvp-season/{pvp_season_id}/pvp-reward/index"
        namespace = f"dynamic-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # PvP Tier API

    def get_pvp_tier_media(self, pvp_tier_id):
        """
        PvP Tier API - Returns media for a PvP tier by ID.
        """
        resource = f"/data/wow/media/pvp-tier/{pvp_tier_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_pvp_tiers_index(self):
        """
        PvP Tier API - Returns an index of PvP tiers.
        """
        resource = f"/data/wow/pvp-tier/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_pvp_tier(self, pvp_tier_id):
        """
        PvP Tier API - Returns a PvP tier by ID.
        """
        resource = f"/data/wow/pvp-tier/{pvp_tier_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Quest API

    def get_quests_index(self):
        """
        Quest API - Returns the parent index for quests.
        """
        resource = f"/data/wow/quest/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_quest(self, quest_id):
        """
        Quest API - Returns a quest by ID.
        """
        resource = f"/data/wow/quest/{quest_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_quest_categories_index(self):
        """
        Quest API - Returns an index of quest categories (such as quests for a specific class,
        profession, or storyline).
        """
        resource = f"/data/wow/quest/category/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_quest_category(self, quest_category_id):
        """
        Quest API - Returns a quest category by ID.
        """
        resource = f"/data/wow/quest/category/{quest_category_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_quest_areas_index(self):
        """
        Quest API - Returns an index of quest areas.
        """
        resource = f"/data/wow/quest/area/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_quest_area(self, quest_area_id):
        """
        Quest API - Returns a quest area by ID.
        """
        resource = f"/data/wow/quest/area/{quest_area_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_quest_types_index(self):
        """
        Quest API - Returns an index of quest types (such as PvP quests, raid quests, or account
        quests).
        """
        resource = f"/data/wow/quest/type/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_quest_type(self, quest_type_id):
        """
        Quest API - Returns a quest type by ID.
        """
        resource = f"/data/wow/quest/type/{quest_type_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Realm API

    def get_realms_index(self):
        """
        Realm API - Returns an index of realms.
        """
        resource = f"/data/wow/realm/index"
        namespace = f"dynamic-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_realm(self, realm_slug):
        """
        Realm API - Returns a single realm by slug or ID.
        """
        resource = f"/data/wow/realm/{realm_slug}"
        namespace = f"dynamic-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Region API

    def get_regions_index(self):
        """
        Region API - Returns an index of regions.
        """
        resource = f"/data/wow/region/index"
        namespace = f"dynamic-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_region(self, region_id):
        """
        Region API - Returns a region by ID.
        """
        resource = f"/data/wow/region/{region_id}"
        namespace = f"dynamic-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Reputations API

    def get_reputation_factions_index(self):
        """
        Reputations API - Returns an index of reputation factions.
        """
        resource = f"/data/wow/reputation-faction/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_reputation_faction(self, reputation_faction_id):
        """
        Reputations API - Returns a single reputation faction by ID.
        """
        resource = f"/data/wow/reputation-faction/{reputation_faction_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_reputation_tiers_index(self):
        """
        Reputations API - Returns an index of reputation tiers.
        """
        resource = f"/data/wow/reputation-tiers/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_reputation_tier(self, reputation_tiers_id):
        """
        Reputations API - Returns a single set of reputation tiers by ID.
        """
        resource = f"/data/wow/reputation-tiers/{reputation_tiers_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Spell API

    def get_spell(self, spell_id):
        """
        Spell API - Returns a spell by ID.
        """
        resource = f"/data/wow/spell/{spell_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_spell_media(self, spell_id):
        """
        Spell API - Returns media for a spell by ID.
        """
        resource = f"/data/wow/media/spell/{spell_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Talent API

    def get_talents_index(self):
        """
        Talent API - Returns an index of talents.
        """
        resource = f"/data/wow/talent/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_talent(self, talent_id):
        """
        Talent API - Returns a talent by ID.
        """
        resource = f"/data/wow/talent/{talent_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_pvp_talents_index(self):
        """
        Talent API - Returns an index of PvP talents.
        """
        resource = f"/data/wow/pvp-talent/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_pvp_talent(self, pvp_talent_id):
        """
        Talent API - Returns a PvP talent by ID.
        """
        resource = f"/data/wow/pvp-talent/{pvp_talent_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Title API

    def get_titles_index(self):
        """
        Title API - Returns an index of titles.
        """
        resource = f"/data/wow/title/index"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_title(self, title_id):
        """
        Title API - Returns a title by ID.
        """
        resource = f"/data/wow/title/{title_id}"
        namespace = f"static-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # WoW Token API

    def get_token_index(self):
        """
        WoW Token API - Returns the WoW Token index.
        """
        resource = f"/data/wow/token/index"
        namespace = f"dynamic-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)
