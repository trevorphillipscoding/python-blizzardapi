class GameDataMixin:
    """All Game Data API methods"""

    # Achievement API

    def get_achievement_categories_index(self):
        """
        Achievement API - Returns an index of achievement categories.
        """
        resource = "/data/wow/achievement-category/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_achievement_category(self, achievement_category_id):
        """
        Achievement API - Returns an achievement category by ID.
        """
        resource = "/data/wow/achievement-category/{0}"
        params = [achievement_category_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_achievements_index(self):
        """
        Achievement API - Returns an index of achievements.
        """
        resource = "/data/wow/achievement/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_achievement(self, achievement_id):
        """
        Achievement API - Returns an achievement by ID.
        """
        resource = "/data/wow/achievement/{0}"
        params = [achievement_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_achievement_media(self, achievement_id):
        """
        Achievement API - Returns media for an achievement by ID.
        """
        resource = "/data/wow/media/achievement/{0}"
        params = [achievement_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    # Auction House API

    def get_auctions(self, connected_realm_id):
        """
        Auction House API - Returns all active auctions for a connected realm.
        """
        resource = "/data/wow/connected-realm/{0}/auctions"
        params = [connected_realm_id]
        namespace = "dynamic-{0}"
        return self.get_resource(resource, namespace, *params)

    # Azerite Essence API

    def get_azerite_essences_index(self):
        """
        Azerite Essence API - Returns an index of azerite essences.
        """
        resource = "/data/wow/azerite-essence/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_azerite_essence(self, azerite_essence_id):
        """
        Azerite Essence API - Returns an azerite essence by ID.
        """
        resource = "/data/wow/azerite-essence/{0}"
        params = [azerite_essence_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_azerite_essence_media(self, azerite_essence_id):
        """
        Azerite Essence API - Returns media for an azerite essence by ID.
        """
        resource = "/data/wow/media/azerite-essence/{0}"
        params = [azerite_essence_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    # Connected Realm API

    def get_connected_realms_index(self):
        """
        Connected Realm API - Returns an index of connected realms.
        """
        resource = "/data/wow/connected-realm/index"
        namespace = "dynamic-{0}"
        return self.get_resource(resource, namespace)

    def get_connected_realm(self, connected_realm_id):
        """
        Connected Realm API - Returns a connected realm by ID.
        """
        resource = "/data/wow/connected-realm/{0}"
        params = [connected_realm_id]
        namespace = "dynamic-{0}"
        return self.get_resource(resource, namespace, *params)

    # Creature API

    def get_creature_families_index(self):
        """
        Creature API - Returns an index of creature families.
        """
        resource = "/data/wow/creature-family/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_creature_family(self, creature_family_id):
        """
        Creature API - Returns a creature family by ID.
        """
        resource = "/data/wow/creature-family/{0}"
        params = [creature_family_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_creature_types_index(self):
        """
        Creature API - Returns an index of creature types.
        """
        resource = "/data/wow/creature-type/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_creature_type(self, creature_type_id):
        """
        Creature API - Returns a creature type by ID.
        """
        resource = "/data/wow/creature-type/{0}"
        params = [creature_type_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_creature(self, creature_id):
        """
        Creature API - Returns a creature by ID.
        """
        resource = "/data/wow/creature/{0}"
        params = [creature_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_creature_display_media(self, creature_display_id):
        """
        Creature API - Returns media for a creature display by ID.
        """
        resource = "/data/wow/media/creature-display/{0}"
        params = [creature_display_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_creature_family_media(self, creature_family_id):
        """
        Creature API - Returns media for a creature family by ID.
        """
        resource = "/data/wow/media/creature-family/{0}"
        params = [creature_family_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    # Guild Crest API

    def get_guild_crest_components_index(self):
        """
        Guild Crest API - Returns an index of guild crest media.
        """
        resource = "/data/wow/guild-crest/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_guild_crest_border_media(self, border_id):
        """
        Guild Crest API - Returns media for a guild crest border by ID.
        """
        resource = "/data/wow/media/guild-crest/border/{0}"
        params = [border_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_guild_crest_emblem_media(self, emblem_id):
        """
        Guild Crest API - Returns media for a guild crest emblem by ID.
        """
        resource = "/data/wow/media/guild-crest/emblem/{0}"
        params = [emblem_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    # Item API

    def get_item_classes_index(self):
        """
        Item API - Returns an index of item classes.
        """
        resource = "/data/wow/item-class/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_item_class(self, item_class_id):
        """
        Item API - Returns an item class by ID.
        """
        resource = "/data/wow/item-class/{0}"
        params = [item_class_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_item_sets_index(self):
        """
        Item API - Returns an index of item sets.
        """
        resource = "/data/wow/item-set/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_item_set(self, item_set_id):
        """
        Item API - Returns an item set by ID.
        """
        resource = "/data/wow/item-set/{0}"
        params = [item_set_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_item_subclass(self, item_class_id, item_subclass_id):
        """
        Item API - Returns an item subclass by ID.
        """
        resource = "/data/wow/item-class/{0}/item-subclass/{1}"
        params = [item_class_id, item_subclass_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_item(self, item_id):
        """
        Item API - Returns an item by ID.
        """
        resource = "/data/wow/item/{0}"
        params = [item_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_item_media(self, item_id):
        """
        Item API - Returns media for an item by ID.
        """
        resource = "/data/wow/media/item/{0}"
        params = [item_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    # Journal API

    def get_journal_expansions_index(self):
        """
        Journal API - Returns an index of journal expansions.
        """
        resource = "/data/wow/journal-expansion/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_journal_expansion(self, journal_expansion_id):
        """
        Journal API - Returns a journal expansion by ID.
        """
        resource = "/data/wow/journal-expansion/{0}"
        params = [journal_expansion_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_journal_encounters_index(self):
        """
        Journal API - Returns an index of journal encounters.
        """
        resource = "/data/wow/journal-encounter/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_journal_encounter(self, journal_encounter_id):
        """
        Journal API - Returns a journal encounter by ID.
        """
        resource = "/data/wow/journal-encounter/{0}"
        params = [journal_encounter_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_journal_instances_index(self):
        """
        Journal API - Returns an index of journal instances.
        """
        resource = "/data/wow/journal-instance/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_journal_instance(self, journal_instance_id):
        """
        Journal API - Returns a journal instance.
        """
        resource = "/data/wow/journal-instance/{0}"
        params = [journal_instance_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_journal_instance_media(self, journal_instance_id):
        """
        Journal API - Returns media for a journal instance by ID.
        """
        resource = "/data/wow/media/journal-instance/{0}"
        params = [journal_instance_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    # Modified Crafting API

    def get_modified_crafting_index(self):
        """
        Modified Crafting API - Returns the parent index for Modified Crafting.
        """
        resource = "/data/wow/modified-crafting/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_modified_crafting_category_index(self):
        """
        Modified Crafting API - Returns the index of Modified Crafting categories.
        """
        resource = "/data/wow/modified-crafting/category/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_modified_crafting_category(self, category_id):
        """
        Modified Crafting API - Returns the index of Modified Crafting categories.
        """
        resource = "/data/wow/modified-crafting/category/{0}"
        params = [category_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_modified_crafting_reagent_slot_type_index(self):
        """
        Modified Crafting API - Returns the index of Modified Crafting reagent slot types.
        """
        resource = "/data/wow/modified-crafting/reagent-slot-type/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_modified_crafting_reagent_slot_type(self, slot_type_id):
        """
        Modified Crafting API - Returns a Modified Crafting reagent slot type by ID.
        """
        resource = "/data/wow/modified-crafting/reagent-slot-type/{0}"
        params = [slot_type_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    # Mount API

    def get_mounts_index(self):
        """
        Mount API - Returns an index of mounts.
        """
        resource = "/data/wow/mount/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_mount(self, mount_id):
        """
        Mount API - Returns a mount by ID.
        """
        resource = "/data/wow/mount/{0}"
        params = [mount_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    # Mythic Keystone Affix API

    def get_mythic_keystone_affixes_index(self):
        """
        Mythic Keystone Affix API - Returns an index of mythic keystone affixes.
        """
        resource = "/data/wow/keystone-affix/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_mythic_keystone_affix(self, keystone_affix_id):
        """
        Mythic Keystone Affix API - Returns a mythic keystone affix by ID.
        """
        resource = "/data/wow/keystone-affix/{0}"
        params = [keystone_affix_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_mythic_keystone_affix_media(self, keystone_affix_id):
        """
        Mythic Keystone Affix API - Returns media for a mythic keystone affix by ID.
        """
        resource = "/data/wow/media/keystone-affix/{0}"
        params = [keystone_affix_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    # Mythic Keystone Dungeon API

    def get_mythic_keystone_dungeons_index(self):
        """
        Mythic Keystone Dungeon API - Returns an index of Mythic Keystone dungeons.
        """
        resource = "/data/wow/mythic-keystone/dungeon/index"
        namespace = "dynamic-{0}"
        return self.get_resource(resource, namespace)

    def get_mythic_keystone_dungeon(self, dungeon_id):
        """
        Mythic Keystone Dungeon API - Returns a Mythic Keystone dungeon by ID.
        """
        resource = "/data/wow/mythic-keystone/dungeon/{0}"
        params = [dungeon_id]
        namespace = "dynamic-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_mythic_keystone_index(self):
        """
        Mythic Keystone Dungeon API - Returns an index of links to other documents related to
        Mythic Keystone dungeons.
        """
        resource = "/data/wow/mythic-keystone/index"
        namespace = "dynamic-{0}"
        return self.get_resource(resource, namespace)

    def get_mythic_keystone_periods_index(self):
        """
        Mythic Keystone Dungeon API - Returns an index of Mythic Keystone periods.
        """
        resource = "/data/wow/mythic-keystone/period/index"
        namespace = "dynamic-{0}"
        return self.get_resource(resource, namespace)

    def get_mythic_keystone_period(self, period_id):
        """
        Mythic Keystone Dungeon API - Returns a Mythic Keystone period by ID.
        """
        resource = "/data/wow/mythic-keystone/period/{0}"
        params = [period_id]
        namespace = "dynamic-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_mythic_keystone_seasons_index(self):
        """
        Mythic Keystone Dungeon API - Returns an index of Mythic Keystone seasons.
        """
        resource = "/data/wow/mythic-keystone/season/index"
        namespace = "dynamic-{0}"
        return self.get_resource(resource, namespace)

    def get_mythic_keystone_season(self, season_id):
        """
        Mythic Keystone Dungeon API - Returns a Mythic Keystone season by ID.
        """
        resource = "/data/wow/mythic-keystone/season/{0}"
        params = [season_id]
        namespace = "dynamic-{0}"
        return self.get_resource(resource, namespace, *params)

    # Mythic Keystone Leaderboard API

    def get_mythic_keystone_leaderboards_index(self, connected_realm_id):
        """
        Mythic Keystone Leaderboard API - Returns an index of Mythic Keystone Leaderboard dungeon
        instances for a connected realm.
        """
        resource = "/data/wow/connected-realm/{0}/mythic-leaderboard/index"
        params = [connected_realm_id]
        namespace = "dynamic-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_mythic_keystone_leaderboard(
        self, connected_realm_id, dungeon_id, period_id
    ):
        """
        Mythic Keystone Leaderboard API - Returns a weekly Mythic Keystone Leaderboard by period.
        """
        resource = "/data/wow/connected-realm/{0}/mythic-leaderboard/{1}/period/{2}"
        params = [connected_realm_id, dungeon_id, period_id]
        namespace = "dynamic-{0}"
        return self.get_resource(resource, namespace, *params)

    # Mythic Raid Leaderboard API

    def get_mythic_raid_leaderboard(self, raid, faction):
        """
        Mythic Raid Leaderboard API - Returns the leaderboard for a given raid and faction.
        """
        resource = "/data/wow/leaderboard/hall-of-fame/{0}/{1}"
        params = [raid, faction]
        namespace = "dynamic-{0}"
        return self.get_resource(resource, namespace, *params)

    # Pet API

    def get_pets_index(self):
        """
        Pet API - Returns an index of battle pets.
        """
        resource = "/data/wow/pet/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_pet(self, pet_id):
        """
        Pet API - Returns a battle pets by ID.
        """
        resource = "/data/wow/pet/{0}"
        params = [pet_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_pet_media(self, pet_id):
        """
        Pet API - Returns media for a battle pet by ID.
        """
        resource = "/data/wow/media/pet/{0}"
        params = [pet_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_pet_abilities_index(self):
        """
        Pet API - Returns an index of pet abilities.
        """
        resource = "/data/wow/pet-ability/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_pet_ability(self, pet_ability_id):
        """
        Pet API - Returns a pet ability by ID.
        """
        resource = "/data/wow/pet-ability/{0}"
        params = [pet_ability_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_pet_ability_media(self, pet_ability_id):
        """
        Pet API - Returns media for a pet ability by ID.
        """
        resource = "/data/wow/media/pet-ability/{0}"
        params = [pet_ability_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    # Playable Class API

    def get_playable_classes_index(self):
        """
        Playable Class API - Returns an index of playable classes.
        """
        resource = "/data/wow/playable-class/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_playable_class(self, class_id):
        """
        Playable Class API - Returns a playable class by ID.
        """
        resource = "/data/wow/playable-class/{0}"
        params = [class_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_playable_class_media(self, playable_class_id):
        """
        Playable Class API - Returns media for a playable class by ID.
        """
        resource = "/data/wow/media/playable-class/{0}"
        params = [playable_class_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_pvp_talent_slots(self, class_id):
        """
        Playable Class API - Returns the PvP talent slots for a playable class by ID.
        """
        resource = "/data/wow/playable-class/{0}/pvp-talent-slots"
        params = [class_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    # Playable Race API

    def get_playable_races_index(self):
        """
        Playable Race API - Returns an index of playable races.
        """
        resource = "/data/wow/playable-race/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_playable_race(self, playable_race_id):
        """
        Playable Race API - Returns a playable race by ID.
        """
        resource = "/data/wow/playable-race/{0}"
        params = [playable_race_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    # Playable Specialization API

    def get_playable_specializations_index(self):
        """
        Playable Specialization API - Returns an index of playable specializations.
        """
        resource = "/data/wow/playable-specialization/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_playable_specialization(self, spec_id):
        """
        Playable Specialization API - Returns a playable specialization by ID.
        """
        resource = "/data/wow/playable-specialization/{0}"
        params = [spec_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_playable_specialization_media(self, spec_id):
        """
        Playable Specialization API - Returns media for a playable specialization by ID.
        """
        resource = "/data/wow/media/playable-specialization/{0}"
        params = [spec_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    # Power Type API

    def get_power_types_index(self):
        """
        Power Type API - Returns an index of power types.
        """
        resource = "/data/wow/power-type/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_power_type(self, power_type_id):
        """
        Power Type API - Returns a power type by ID.
        """
        resource = "/data/wow/power-type/{0}"
        params = [power_type_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    # Profession API

    def get_professions_index(self):
        """
        Profession API - Returns an index of professions.
        """
        resource = "/data/wow/profession/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_profession(self, profession_id):
        """
        Profession API - Returns a profession by ID.
        """
        resource = "/data/wow/profession/{0}"
        params = [profession_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_profession_media(self, profession_id):
        """
        Profession API - Returns media for a profession by ID.
        """
        resource = "/data/wow/media/profession/{0}"
        params = [profession_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_profession_skill_tier(self, profession_id, skill_tier_id):
        """
        Profession API - Returns a skill tier for a profession by ID.
        """
        resource = "/data/wow/profession/{0}/skill-tier/{1}"
        params = [profession_id, skill_tier_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_recipe(self, recipe_id):
        """
        Profession API - Returns a recipe by ID.
        """
        resource = "/data/wow/recipe/{0}"
        params = [recipe_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_recipe_media(self, recipe_id):
        """
        Profession API - Returns media for a recipe by ID.
        """
        resource = "/data/wow/media/recipe/{0}"
        params = [recipe_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    # PvP Season API

    def get_pvp_seasons_index(self):
        """
        PvP Season API - Returns an index of PvP seasons.
        """
        resource = "/data/wow/pvp-season/index"
        namespace = "dynamic-{0}"
        return self.get_resource(resource, namespace)

    def get_pvp_season(self, pvp_season_id):
        """
        PvP Season API - Returns a PvP season by ID.
        """
        resource = "/data/wow/pvp-season/{0}"
        params = [pvp_season_id]
        namespace = "dynamic-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_pvp_leaderboards_index(self, pvp_season_id):
        """
        PvP Season API - Returns an index of PvP leaderboards for a PvP season.
        """
        resource = "/data/wow/pvp-season/{0}/pvp-leaderboard/index"
        params = [pvp_season_id]
        namespace = "dynamic-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_pvp_leaderboard(self, pvp_season_id, pvp_bracket):
        """
        PvP Season API - Returns the PvP leaderboard of a specific PvP bracket for a PvP season.
        """
        resource = "/data/wow/pvp-season/{0}/pvp-leaderboard/{1}"
        params = [pvp_season_id, pvp_bracket]
        namespace = "dynamic-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_pvp_rewards_index(self, pvp_season_id):
        """
        PvP Season API - Returns an index of PvP rewards for a PvP season.
        """
        resource = "/data/wow/pvp-season/{0}/pvp-reward/index"
        params = [pvp_season_id]
        namespace = "dynamic-{0}"
        return self.get_resource(resource, namespace, *params)

    # PvP Tier API

    def get_pvp_tier_media(self, pvp_tier_id):
        """
        PvP Tier API - Returns media for a PvP tier by ID.
        """
        resource = "/data/wow/media/pvp-tier/{0}"
        params = [pvp_tier_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_pvp_tiers_index(self):
        """
        PvP Tier API - Returns an index of PvP tiers.
        """
        resource = "/data/wow/pvp-tier/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_pvp_tier(self, pvp_tier_id):
        """
        PvP Tier API - Returns a PvP tier by ID.
        """
        resource = "/data/wow/pvp-tier/{0}"
        params = [pvp_tier_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    # Quest API

    def get_quests_index(self):
        """
        Quest API - Returns the parent index for quests.
        """
        resource = "/data/wow/quest/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_quest(self, quest_id):
        """
        Quest API - Returns a quest by ID.
        """
        resource = "/data/wow/quest/{0}"
        params = [quest_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_quest_categories_index(self):
        """
        Quest API - Returns an index of quest categories (such as quests for a specific class,
        profession, or storyline).
        """
        resource = "/data/wow/quest/category/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_quest_category(self, quest_category_id):
        """
        Quest API - Returns a quest category by ID.
        """
        resource = "/data/wow/quest/category/{0}"
        params = [quest_category_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_quest_areas_index(self):
        """
        Quest API - Returns an index of quest areas.
        """
        resource = "/data/wow/quest/area/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_quest_area(self, quest_area_id):
        """
        Quest API - Returns a quest area by ID.
        """
        resource = "/data/wow/quest/area/{0}"
        params = [quest_area_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_quest_types_index(self):
        """
        Quest API - Returns an index of quest types (such as PvP quests, raid quests, or account
        quests).
        """
        resource = "/data/wow/quest/type/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_quest_type(self, quest_type_id):
        """
        Quest API - Returns a quest type by ID.
        """
        resource = "/data/wow/quest/type/{0}"
        params = [quest_type_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    # Realm API

    def get_realms_index(self):
        """
        Realm API - Returns an index of realms.
        """
        resource = "/data/wow/realm/index"
        namespace = "dynamic-{0}"
        return self.get_resource(resource, namespace)

    def get_realm(self, realm_slug):
        """
        Realm API - Returns a single realm by slug or ID.
        """
        resource = "/data/wow/realm/{0}"
        params = [realm_slug]
        namespace = "dynamic-{0}"
        return self.get_resource(resource, namespace, *params)

    # Region API

    def get_regions_index(self):
        """
        Region API - Returns an index of regions.
        """
        resource = "/data/wow/region/index"
        namespace = "dynamic-{0}"
        return self.get_resource(resource, namespace)

    def get_region(self, region_id):
        """
        Region API - Returns a region by ID.
        """
        resource = "/data/wow/region/{0}"
        params = [region_id]
        namespace = "dynamic-{0}"
        return self.get_resource(resource, namespace, *params)

    # Reputations API

    def get_reputation_factions_index(self):
        """
        Reputations API - Returns an index of reputation factions.
        """
        resource = "/data/wow/reputation-faction/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_reputation_faction(self, reputation_faction_id):
        """
        Reputations API - Returns a single reputation faction by ID.
        """
        resource = "/data/wow/reputation-faction/{0}"
        params = [reputation_faction_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_reputation_tiers_index(self):
        """
        Reputations API - Returns an index of reputation tiers.
        """
        resource = "/data/wow/reputation-tiers/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_reputation_tier(self, reputation_tiers_id):
        """
        Reputations API - Returns a single set of reputation tiers by ID.
        """
        resource = "/data/wow/reputation-tiers/{0}"
        params = [reputation_tiers_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    # Spell API

    def get_spell(self, spell_id):
        """
        Spell API - Returns a spell by ID.
        """
        resource = "/data/wow/spell/{0}"
        params = [spell_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_spell_media(self, spell_id):
        """
        Spell API - Returns media for a spell by ID.
        """
        resource = "/data/wow/media/spell/{0}"
        params = [spell_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    # Talent API

    def get_talents_index(self):
        """
        Talent API - Returns an index of talents.
        """
        resource = "/data/wow/talent/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_talent(self, talent_id):
        """
        Talent API - Returns a talent by ID.
        """
        resource = "/data/wow/talent/{0}"
        params = [talent_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    def get_pvp_talents_index(self):
        """
        Talent API - Returns an index of PvP talents.
        """
        resource = "/data/wow/pvp-talent/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_pvp_talent(self, pvp_talent_id):
        """
        Talent API - Returns a PvP talent by ID.
        """
        resource = "/data/wow/pvp-talent/{0}"
        params = [pvp_talent_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    # Title API

    def get_titles_index(self):
        """
        Title API - Returns an index of titles.
        """
        resource = "/data/wow/title/index"
        namespace = "static-{0}"
        return self.get_resource(resource, namespace)

    def get_title(self, title_id):
        """
        Title API - Returns a title by ID.
        """
        resource = "/data/wow/title/{0}"
        params = [title_id]
        namespace = "static-{0}"
        return self.get_resource(resource, namespace, *params)

    # WoW Token API

    def get_token_index(self):
        """
        WoW Token API - Returns the WoW Token index.
        """
        resource = "/data/wow/token/index"
        namespace = "dynamic-{0}"
        return self.get_resource(resource, namespace)
