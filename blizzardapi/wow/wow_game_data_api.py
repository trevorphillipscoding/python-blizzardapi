from ..api import Api


class WowGameDataApi(Api):
    """All Game Data API methods"""

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    # Achievement API

    def get_achievement_categories_index(self, region, locale):
        """
        Achievement API - Returns an index of achievement categories.
        """
        resource = "/data/wow/achievement-category/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_achievement_category(
        self, region, locale, achievement_category_id
    ):
        """
        Achievement API - Returns an achievement category by ID.
        """
        resource = f"/data/wow/achievement-category/{achievement_category_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_achievements_index(self, region, locale):
        """
        Achievement API - Returns an index of achievements.
        """
        resource = "/data/wow/achievement/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_achievement(self, region, locale, achievement_id):
        """
        Achievement API - Returns an achievement by ID.
        """
        resource = f"/data/wow/achievement/{achievement_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_achievement_media(self, region, locale, achievement_id):
        """
        Achievement API - Returns media for an achievement by ID.
        """
        resource = f"/data/wow/media/achievement/{achievement_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Auction House API

    def get_auctions(self, region, locale, connected_realm_id):
        """
        Auction House API - Returns all active auctions for a connected realm.
        """
        resource = f"/data/wow/connected-realm/{connected_realm_id}/auctions"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Azerite Essence API

    def get_azerite_essences_index(self, region, locale):
        """
        Azerite Essence API - Returns an index of azerite essences.
        """
        resource = "/data/wow/azerite-essence/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_azerite_essence(self, region, locale, azerite_essence_id):
        """
        Azerite Essence API - Returns an azerite essence by ID.
        """
        resource = f"/data/wow/azerite-essence/{azerite_essence_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_azerite_essence_media(self, region, locale, azerite_essence_id):
        """
        Azerite Essence API - Returns media for an azerite essence by ID.
        """
        resource = f"/data/wow/media/azerite-essence/{azerite_essence_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Connected Realm API

    def get_connected_realms_index(self, region, locale):
        """
        Connected Realm API - Returns an index of connected realms.
        """
        resource = "/data/wow/connected-realm/index"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_connected_realm(self, region, locale, connected_realm_id):
        """
        Connected Realm API - Returns a connected realm by ID.
        """
        resource = f"/data/wow/connected-realm/{connected_realm_id}"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Creature API

    def get_creature_families_index(self, region, locale):
        """
        Creature API - Returns an index of creature families.
        """
        resource = "/data/wow/creature-family/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_creature_family(self, region, locale, creature_family_id):
        """
        Creature API - Returns a creature family by ID.
        """
        resource = f"/data/wow/creature-family/{creature_family_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_creature_types_index(self, region, locale):
        """
        Creature API - Returns an index of creature types.
        """
        resource = "/data/wow/creature-type/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_creature_type(self, region, locale, creature_type_id):
        """
        Creature API - Returns a creature type by ID.
        """
        resource = f"/data/wow/creature-type/{creature_type_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_creature(self, region, locale, creature_id):
        """
        Creature API - Returns a creature by ID.
        """
        resource = f"/data/wow/creature/{creature_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_creature_display_media(self, region, locale, creature_display_id):
        """
        Creature API - Returns media for a creature display by ID.
        """
        resource = f"/data/wow/media/creature-display/{creature_display_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_creature_family_media(self, region, locale, creature_family_id):
        """
        Creature API - Returns media for a creature family by ID.
        """
        resource = f"/data/wow/media/creature-family/{creature_family_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Guild Crest API

    def get_guild_crest_components_index(self, region, locale):
        """
        Guild Crest API - Returns an index of guild crest media.
        """
        resource = "/data/wow/guild-crest/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_guild_crest_border_media(self, region, locale, border_id):
        """
        Guild Crest API - Returns media for a guild crest border by ID.
        """
        resource = f"/data/wow/media/guild-crest/border/{border_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_guild_crest_emblem_media(self, region, locale, emblem_id):
        """
        Guild Crest API - Returns media for a guild crest emblem by ID.
        """
        resource = f"/data/wow/media/guild-crest/emblem/{emblem_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Item API

    def get_item_classes_index(self, region, locale):
        """
        Item API - Returns an index of item classes.
        """
        resource = "/data/wow/item-class/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item_class(self, region, locale, item_class_id):
        """
        Item API - Returns an item class by ID.
        """
        resource = f"/data/wow/item-class/{item_class_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item_sets_index(self, region, locale):
        """
        Item API - Returns an index of item sets.
        """
        resource = "/data/wow/item-set/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item_set(self, region, locale, item_set_id):
        """
        Item API - Returns an item set by ID.
        """
        resource = f"/data/wow/item-set/{item_set_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item_subclass(
        self, region, locale, item_class_id, item_subclass_id
    ):
        """
        Item API - Returns an item subclass by ID.
        """
        resource = f"/data/wow/item-class/{item_class_id}/item-subclass/{item_subclass_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item(self, region, locale, item_id):
        """
        Item API - Returns an item by ID.
        """
        resource = f"/data/wow/item/{item_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item_media(self, region, locale, item_id):
        """
        Item API - Returns media for an item by ID.
        """
        resource = f"/data/wow/media/item/{item_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Journal API

    def get_journal_expansions_index(self, region, locale):
        """
        Journal API - Returns an index of journal expansions.
        """
        resource = "/data/wow/journal-expansion/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_journal_expansion(self, region, locale, journal_expansion_id):
        """
        Journal API - Returns a journal expansion by ID.
        """
        resource = f"/data/wow/journal-expansion/{journal_expansion_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_journal_encounters_index(self, region, locale):
        """
        Journal API - Returns an index of journal encounters.
        """
        resource = "/data/wow/journal-encounter/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_journal_encounter(self, region, locale, journal_encounter_id):
        """
        Journal API - Returns a journal encounter by ID.
        """
        resource = f"/data/wow/journal-encounter/{journal_encounter_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_journal_instances_index(self, region, locale):
        """
        Journal API - Returns an index of journal instances.
        """
        resource = "/data/wow/journal-instance/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_journal_instance(self, region, locale, journal_instance_id):
        """
        Journal API - Returns a journal instance.
        """
        resource = f"/data/wow/journal-instance/{journal_instance_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_journal_instance_media(self, region, locale, journal_instance_id):
        """
        Journal API - Returns media for a journal instance by ID.
        """
        resource = f"/data/wow/media/journal-instance/{journal_instance_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Modified Crafting API

    def get_modified_crafting_index(self, region, locale):
        """
        Modified Crafting API - Returns the parent index for Modified Crafting.
        """
        resource = "/data/wow/modified-crafting/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_modified_crafting_category_index(self, region, locale):
        """
        Modified Crafting API - Returns the index of Modified Crafting
        categories.
        """
        resource = "/data/wow/modified-crafting/category/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_modified_crafting_category(self, region, locale, category_id):
        """
        Modified Crafting API - Returns the index of Modified Crafting
        categories.
        """
        resource = f"/data/wow/modified-crafting/category/{category_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_modified_crafting_reagent_slot_type_index(self, region, locale):
        """
        Modified Crafting API - Returns the index of Modified Crafting reagent
        slot types.
        """
        resource = "/data/wow/modified-crafting/reagent-slot-type/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_modified_crafting_reagent_slot_type(
        self, region, locale, slot_type_id
    ):
        """
        Modified Crafting API - Returns a Modified Crafting reagent slot type
        by ID.
        """
        resource = (
            f"/data/wow/modified-crafting/reagent-slot-type/{slot_type_id}"
        )
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Mount API

    def get_mounts_index(self, region, locale):
        """
        Mount API - Returns an index of mounts.
        """
        resource = "/data/wow/mount/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mount(self, region, locale, mount_id):
        """
        Mount API - Returns a mount by ID.
        """
        resource = f"/data/wow/mount/{mount_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Mythic Keystone Affix API

    def get_mythic_keystone_affixes_index(self, region, locale):
        """
        Mythic Keystone Affix API - Returns an index of mythic keystone
        affixes.
        """
        resource = "/data/wow/keystone-affix/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_affix(self, region, locale, keystone_affix_id):
        """
        Mythic Keystone Affix API - Returns a mythic keystone affix by ID.
        """
        resource = f"/data/wow/keystone-affix/{keystone_affix_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_affix_media(
        self, region, locale, keystone_affix_id
    ):
        """
        Mythic Keystone Affix API - Returns media for a mythic keystone affix
        by ID.
        """
        resource = f"/data/wow/media/keystone-affix/{keystone_affix_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Mythic Keystone Dungeon API

    def get_mythic_keystone_dungeons_index(self, region, locale):
        """
        Mythic Keystone Dungeon API - Returns an index of Mythic Keystone
        dungeons.
        """
        resource = "/data/wow/mythic-keystone/dungeon/index"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_dungeon(self, region, locale, dungeon_id):
        """
        Mythic Keystone Dungeon API - Returns a Mythic Keystone dungeon by ID.
        """
        resource = f"/data/wow/mythic-keystone/dungeon/{dungeon_id}"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_index(self, region, locale):
        """
        Mythic Keystone Dungeon API - Returns an index of links to other
        documents related to
        Mythic Keystone dungeons.
        """
        resource = "/data/wow/mythic-keystone/index"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_periods_index(self, region, locale):
        """
        Mythic Keystone Dungeon API - Returns an index of Mythic Keystone
        periods.
        """
        resource = "/data/wow/mythic-keystone/period/index"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_period(self, region, locale, period_id):
        """
        Mythic Keystone Dungeon API - Returns a Mythic Keystone period by ID.
        """
        resource = f"/data/wow/mythic-keystone/period/{period_id}"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_seasons_index(self, region, locale):
        """
        Mythic Keystone Dungeon API - Returns an index of Mythic Keystone
        seasons.
        """
        resource = "/data/wow/mythic-keystone/season/index"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_season(self, region, locale, season_id):
        """
        Mythic Keystone Dungeon API - Returns a Mythic Keystone season by ID.
        """
        resource = f"/data/wow/mythic-keystone/season/{season_id}"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Mythic Keystone Leaderboard API

    def get_mythic_keystone_leaderboards_index(
        self, region, locale, connected_realm_id
    ):
        """
        Mythic Keystone Leaderboard API - Returns an index of Mythic Keystone
        Leaderboard dungeon instances for a connected realm.
        """
        resource = f"/data/wow/connected-realm/{connected_realm_id}/mythic-leaderboard/index"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_mythic_keystone_leaderboard(
        self, region, locale, connected_realm_id, dungeon_id, period_id
    ):
        """
        Mythic Keystone Leaderboard API - Returns a weekly Mythic Keystone
        Leaderboard by period.
        """
        resource = f"/data/wow/connected-realm/{connected_realm_id}/mythic-leaderboard/{dungeon_id}/period/{period_id}"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Mythic Raid Leaderboard API

    def get_mythic_raid_leaderboard(self, region, locale, raid, faction):
        """
        Mythic Raid Leaderboard API - Returns the leaderboard for a given raid
        and faction.
        """
        resource = f"/data/wow/leaderboard/hall-of-fame/{raid}/{faction}"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Pet API

    def get_pets_index(self, region, locale):
        """
        Pet API - Returns an index of battle pets.
        """
        resource = "/data/wow/pet/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pet(self, region, locale, pet_id):
        """
        Pet API - Returns a battle pets by ID.
        """
        resource = f"/data/wow/pet/{pet_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pet_media(self, region, locale, pet_id):
        """
        Pet API - Returns media for a battle pet by ID.
        """
        resource = f"/data/wow/media/pet/{pet_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pet_abilities_index(self, region, locale):
        """
        Pet API - Returns an index of pet abilities.
        """
        resource = "/data/wow/pet-ability/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pet_ability(self, region, locale, pet_ability_id):
        """
        Pet API - Returns a pet ability by ID.
        """
        resource = f"/data/wow/pet-ability/{pet_ability_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pet_ability_media(self, region, locale, pet_ability_id):
        """
        Pet API - Returns media for a pet ability by ID.
        """
        resource = f"/data/wow/media/pet-ability/{pet_ability_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Playable Class API

    def get_playable_classes_index(self, region, locale):
        """
        Playable Class API - Returns an index of playable classes.
        """
        resource = "/data/wow/playable-class/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_playable_class(self, region, locale, class_id):
        """
        Playable Class API - Returns a playable class by ID.
        """
        resource = f"/data/wow/playable-class/{class_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_playable_class_media(self, region, locale, playable_class_id):
        """
        Playable Class API - Returns media for a playable class by ID.
        """
        resource = f"/data/wow/media/playable-class/{playable_class_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_talent_slots(self, region, locale, class_id):
        """
        Playable Class API - Returns the PvP talent slots for a playable class
        by ID.
        """
        resource = f"/data/wow/playable-class/{class_id}/pvp-talent-slots"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Playable Race API

    def get_playable_races_index(self, region, locale):
        """
        Playable Race API - Returns an index of playable races.
        """
        resource = "/data/wow/playable-race/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_playable_race(self, region, locale, playable_race_id):
        """
        Playable Race API - Returns a playable race by ID.
        """
        resource = f"/data/wow/playable-race/{playable_race_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Playable Specialization API

    def get_playable_specializations_index(self, region, locale):
        """
        Playable Specialization API - Returns an index of playable
        specializations.
        """
        resource = "/data/wow/playable-specialization/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_playable_specialization(self, region, locale, spec_id):
        """
        Playable Specialization API - Returns a playable specialization by ID.
        """
        resource = f"/data/wow/playable-specialization/{spec_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_playable_specialization_media(self, region, locale, spec_id):
        """
        Playable Specialization API - Returns media for a playable
        specialization by ID.
        """
        resource = f"/data/wow/media/playable-specialization/{spec_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Power Type API

    def get_power_types_index(self, region, locale):
        """
        Power Type API - Returns an index of power types.
        """
        resource = "/data/wow/power-type/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_power_type(self, region, locale, power_type_id):
        """
        Power Type API - Returns a power type by ID.
        """
        resource = f"/data/wow/power-type/{power_type_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Profession API

    def get_professions_index(self, region, locale):
        """
        Profession API - Returns an index of professions.
        """
        resource = "/data/wow/profession/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_profession(self, region, locale, profession_id):
        """
        Profession API - Returns a profession by ID.
        """
        resource = f"/data/wow/profession/{profession_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_profession_media(self, region, locale, profession_id):
        """
        Profession API - Returns media for a profession by ID.
        """
        resource = f"/data/wow/media/profession/{profession_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_profession_skill_tier(
        self, region, locale, profession_id, skill_tier_id
    ):
        """
        Profession API - Returns a skill tier for a profession by ID.
        """
        resource = (
            f"/data/wow/profession/{profession_id}/skill-tier/{skill_tier_id}"
        )
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_recipe(self, region, locale, recipe_id):
        """
        Profession API - Returns a recipe by ID.
        """
        resource = f"/data/wow/recipe/{recipe_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_recipe_media(self, region, locale, recipe_id):
        """
        Profession API - Returns media for a recipe by ID.
        """
        resource = f"/data/wow/media/recipe/{recipe_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # PvP Season API

    def get_pvp_seasons_index(self, region, locale):
        """
        PvP Season API - Returns an index of PvP seasons.
        """
        resource = "/data/wow/pvp-season/index"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_season(self, region, locale, pvp_season_id):
        """
        PvP Season API - Returns a PvP season by ID.
        """
        resource = f"/data/wow/pvp-season/{pvp_season_id}"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_leaderboards_index(self, region, locale, pvp_season_id):
        """
        PvP Season API - Returns an index of PvP leaderboards for a PvP season.
        """
        resource = (
            f"/data/wow/pvp-season/{pvp_season_id}/pvp-leaderboard/index"
        )
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_leaderboard(self, region, locale, pvp_season_id, pvp_bracket):
        """
        PvP Season API - Returns the PvP leaderboard of a specific PvP bracket
        for a PvP season.
        """
        resource = f"/data/wow/pvp-season/{pvp_season_id}/pvp-leaderboard/{pvp_bracket}"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_rewards_index(self, region, locale, pvp_season_id):
        """
        PvP Season API - Returns an index of PvP rewards for a PvP season.
        """
        resource = f"/data/wow/pvp-season/{pvp_season_id}/pvp-reward/index"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # PvP Tier API

    def get_pvp_tier_media(self, region, locale, pvp_tier_id):
        """
        PvP Tier API - Returns media for a PvP tier by ID.
        """
        resource = f"/data/wow/media/pvp-tier/{pvp_tier_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_tiers_index(self, region, locale):
        """
        PvP Tier API - Returns an index of PvP tiers.
        """
        resource = "/data/wow/pvp-tier/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_tier(self, region, locale, pvp_tier_id):
        """
        PvP Tier API - Returns a PvP tier by ID.
        """
        resource = f"/data/wow/pvp-tier/{pvp_tier_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Quest API

    def get_quests_index(self, region, locale):
        """
        Quest API - Returns the parent index for quests.
        """
        resource = "/data/wow/quest/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_quest(self, region, locale, quest_id):
        """
        Quest API - Returns a quest by ID.
        """
        resource = f"/data/wow/quest/{quest_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_quest_categories_index(self, region, locale):
        """
        Quest API - Returns an index of quest categories (such as quests for a
        specific class,
        profession, or storyline).
        """
        resource = "/data/wow/quest/category/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_quest_category(self, region, locale, quest_category_id):
        """
        Quest API - Returns a quest category by ID.
        """
        resource = f"/data/wow/quest/category/{quest_category_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_quest_areas_index(self, region, locale):
        """
        Quest API - Returns an index of quest areas.
        """
        resource = "/data/wow/quest/area/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_quest_area(self, region, locale, quest_area_id):
        """
        Quest API - Returns a quest area by ID.
        """
        resource = f"/data/wow/quest/area/{quest_area_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_quest_types_index(self, region, locale):
        """
        Quest API - Returns an index of quest types (such as PvP quests, raid
        quests, or account
        quests).
        """
        resource = "/data/wow/quest/type/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_quest_type(self, region, locale, quest_type_id):
        """
        Quest API - Returns a quest type by ID.
        """
        resource = f"/data/wow/quest/type/{quest_type_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Realm API

    def get_realms_index(self, region, locale):
        """
        Realm API - Returns an index of realms.
        """
        resource = "/data/wow/realm/index"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_realm(self, region, locale, realm_slug):
        """
        Realm API - Returns a single realm by slug or ID.
        """
        resource = f"/data/wow/realm/{realm_slug}"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Region API

    def get_regions_index(self, region, locale):
        """
        Region API - Returns an index of regions.
        """
        resource = "/data/wow/region/index"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_region(self, region, locale, region_id):
        """
        Region API - Returns a region by ID.
        """
        resource = f"/data/wow/region/{region_id}"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Reputations API

    def get_reputation_factions_index(self, region, locale):
        """
        Reputations API - Returns an index of reputation factions.
        """
        resource = "/data/wow/reputation-faction/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_reputation_faction(self, region, locale, reputation_faction_id):
        """
        Reputations API - Returns a single reputation faction by ID.
        """
        resource = f"/data/wow/reputation-faction/{reputation_faction_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_reputation_tiers_index(self, region, locale):
        """
        Reputations API - Returns an index of reputation tiers.
        """
        resource = "/data/wow/reputation-tiers/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_reputation_tier(self, region, locale, reputation_tiers_id):
        """
        Reputations API - Returns a single set of reputation tiers by ID.
        """
        resource = f"/data/wow/reputation-tiers/{reputation_tiers_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Spell API

    def get_spell(self, region, locale, spell_id):
        """
        Spell API - Returns a spell by ID.
        """
        resource = f"/data/wow/spell/{spell_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_spell_media(self, region, locale, spell_id):
        """
        Spell API - Returns media for a spell by ID.
        """
        resource = f"/data/wow/media/spell/{spell_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Talent API

    def get_talents_index(self, region, locale):
        """
        Talent API - Returns an index of talents.
        """
        resource = "/data/wow/talent/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_talent(self, region, locale, talent_id):
        """
        Talent API - Returns a talent by ID.
        """
        resource = f"/data/wow/talent/{talent_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_talents_index(self, region, locale):
        """
        Talent API - Returns an index of PvP talents.
        """
        resource = "/data/wow/pvp-talent/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_pvp_talent(self, region, locale, pvp_talent_id):
        """
        Talent API - Returns a PvP talent by ID.
        """
        resource = f"/data/wow/pvp-talent/{pvp_talent_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # Title API

    def get_titles_index(self, region, locale):
        """
        Title API - Returns an index of titles.
        """
        resource = "/data/wow/title/index"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_title(self, region, locale, title_id):
        """
        Title API - Returns a title by ID.
        """
        resource = f"/data/wow/title/{title_id}"
        query_params = {"namespace": f"static-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)

    # WoW Token API

    def get_token_index(self, region, locale):
        """
        WoW Token API - Returns the WoW Token index.
        """
        resource = "/data/wow/token/index"
        query_params = {"namespace": f"dynamic-{region}", "locale": locale}
        return super().get_resource(resource, region, query_params)
