from ...api import Api


class ProfileApi(Api):
    """All Profile API methods"""

    def __init__(self, region, locale, client_id, client_secret, access_token):
        super().__init__(region, client_id, client_secret, access_token)
        self._locale = locale

    # Account Profile API

    def get_account_profile_summary(self):
        """
        Account Profile API - Returns a profile summary for an account.
        """
        resource = f"/profile/user/wow"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_protected_character_profile_summary(self, realm_id, character_id):
        """
        Account Profile API - Returns a protected profile summary for a character.
        """
        resource = f"/profile/user/wow/protected-character/{realm_id}-{character_id}"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_account_collections_index(self):
        """
        Account Profile API - Returns an index of collection types for an account.
        """
        resource = f"/profile/user/wow/collections"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_account_mounts_collection_summary(self):
        """
        Account Profile API - Returns a summary of the mounts an account has obtained.
        """
        resource = f"/profile/user/wow/collections/mounts"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_account_pets_collection_summary(self):
        """
        Account Profile API - Returns a summary of the battle pets an account has obtained.
        """
        resource = f"/profile/user/wow/collections/pets"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Character Achievements API

    def get_character_achievements_summary(self, realm_slug, character_name):
        """
        Character Achievements API - Returns a summary of the achievements a character has completed.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/achievements"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    def get_character_achievement_statistics(self, realm_slug, character_name):
        """
        Character Achievements API - Returns a character's statistics as they pertain to achievements.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/achievements/statistics"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Character Appearance API

    def get_character_appearance_summary(self, realm_slug, character_name):
        """
        Character Appearance API - Returns a summary of a character's appearance settings.
        """
        resource = f"/profile/wow/character/{realm_slug}/{realm_slug}/appearance"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource, namespace=namespace, locale=self._locale)

    # Character Collections API

    def get_character_collections_index(self, realm_slug, character_name):
        """
        Character Collections API - Returns an index of collection types for a character.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/collections"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)

    def get_character_mounts_collection_index(self, realm_slug, character_name):
        """
        Character Collections API - Returns a summary of the mounts a character has obtained.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/collections/mounts"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)

    def get_character_pets_collection_index(self, realm_slug, character_name):
        """
        Character Collections API - Returns a summary of the battle pets a character has obtained.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/collections/pets"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)

    # Character Encounters API

    def get_character_encounters_summary(self, realm_slug, character_name):
        """
        Character Encounters API - Returns a summary of a character's encounters.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/encounters"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)

    def get_character_dungeons(self, realm_slug, character_name):
        """
        Character Encounters API - Returns a summary of a character's completed dungeons.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/encounters/dungeons"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)

    def get_character_raids(self, realm_slug, character_name):
        """
        Character Encounters API - Returns a summary of a character's completed raids.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/encounters/raids"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)

    # Character Equipment API

    def get_character_equipment_summary(self, realm_slug, character_name):
        """
        Character Equipment API - Returns a summary of the items equipped by a character.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/equipment"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)

    # Character Hunter Pets API

    def get_character_hunter_pets_summary(self, realm_slug, character_name):
        """
        Character Hunter Pets API - If the character is a hunter, returns a summary of the character's hunter pets.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/hunter-pets"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)

    # Character Media API

    def get_character_media_summary(self, realm_slug, character_name):
        """
        Character Media API - Returns a summary of the media assets available for a character (such as an avatar render).
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/character-media"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)

    # Character Mythic Keystone Profile API

    def get_character_mythic_keystone_profile_index(self, realm_slug, character_name):
        """
        Character Mythic Keystone Profile API - Returns the Mythic Keystone profile index for a character.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/mythic-keystone-profile"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)

    def get_character_mythic_keystone_profile_season_details(
        self, realm_slug, character_name, season_id
    ):
        """
        Character Mythic Keystone Profile API - Returns the Mythic Keystone season details for a character.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/mythic-keystone-profile/season/{season_id}"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)

    # Character Professions API

    def get_character_professions_summary(self, realm_slug, character_name):
        """
        Character Professions API - Returns a summary of professions for a character.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/professions"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)

    # Character Profile API

    def get_character_profile_summary(self, realm_slug, character_name):
        """
        Character Profile API - Returns a profile summary for a character.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)

    def get_character_profile_status(self, realm_slug, character_name):
        """
        Character Profile API - Returns the status and a unique ID for a character.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/status"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)

    # Character PvP API

    def get_character_pvp_bracket_statistics(
        self, realm_slug, character_name, pvp_bracket
    ):
        """
        Character PvP API - Returns the PvP bracket statistics for a character.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/pvp-bracket/{pvp_bracket}"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)

    def get_character_pvp_summary(self, realm_slug, character_name):
        """
        Character PvP API - Returns a PvP summary for a character.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/pvp-summary"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)

    # Character Quests API

    def get_character_quests(self, realm_slug, character_name):
        """
        Character Quests API - Returns a character's active quests as well as a link to the character's completed quests.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/quests"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)

    def get_character_completed_quests(self, realm_slug, character_name):
        """
        Character Quests API - Returns a list of quests that a character has completed.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/quests/completed"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)

    # Character Reputations API

    def get_character_reputations_summary(self, realm_slug, character_name):
        """
        Character Reputations API - Returns a summary of a character's reputations.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/reputations"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)

    # Character Specializations API

    def get_character_specializations_summary(self, realm_slug, character_name):
        """
        Character Specializations API - Returns a summary of a character's specializations.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/specializations"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)

    # Character Statistics API

    def get_character_statistics_summary(self, realm_slug, character_name):
        """
        Character Statistics API - Returns a statistics summary for a character.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/statistics"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)

    # Character Titles API

    def get_character_titles_summary(self, realm_slug, character_name):
        """
        Character Titles API - Returns a summary of titles a character has obtained.
        """
        resource = f"/profile/wow/character/{realm_slug}/{character_name}/titles"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)

    # Guild API

    def get_guild(self, realm_slug, name_slug):
        """
        Guild API - Returns a single guild by its name and realm.
        """
        resource = f"/data/wow/guild/{realm_slug}/{name_slug}"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)

    def get_guild_activity(self, realm_slug, name_slug):
        """
        Guild API - Returns a single guild's activity by name and realm.
        """
        resource = f"/data/wow/guild/{realm_slug}/{name_slug}/activity"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)

    def get_guild_achievements(self, realm_slug, name_slug):
        """
        Guild API - Returns a single guild's achievements by name and realm.
        """
        resource = f"/data/wow/guild/{realm_slug}/{name_slug}/achievements"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)

    def get_guild_roster(self, realm_slug, name_slug):
        """
        Guild API - Returns a single guild's roster by its name and realm.
        """
        resource = f"/data/wow/guild/{realm_slug}/{name_slug}/roster"
        namespace = f"profile-{self.region}"
        return super().get_resource(resource,  namespace=namespace, locale=self._locale)
