class ProfileMixin:
    """All Profile API methods"""

    # Account Profile API

    def get_account_profile_summary(self):
        """
        Account Profile API - Returns a profile summary for an account.
        """
        resource = "profile/user/wow"
        namespace = "profile-{0}"
        return self.get_resource(resource)

    def get_protected_character_profile_summary(self, realm_id, character_id):
        """
        Account Profile API - Returns a protected profile summary for a character.
        """
        resource = "profile/user/wow/protected-character/{0}-{1}"
        params = [realm_id, character_id]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    def get_account_collection_index(self):
        """
        Account Profile API - Returns an index of collection types for an account.
        """
        resource = "profile/user/wow/collections"
        namespace = "profile-{0}"
        return self.get_resource(resource)

    def get_mount_collection_summary(self):
        """
        Account Profile API - Returns a summary of the mounts an account has obtained.
        """
        resource = "profile/user/wow/collections/mounts"
        namespace = "profile-{0}"
        return self.get_resource(resource)

    def get_pet_collection_summary(self):
        """
        Account Profile API - Returns a summary of the battle pets an account has obtained.
        """
        resource = "profile/user/wow/collections/pets"
        namespace = "profile-{0}"
        return self.get_resource(resource)

    # Character Achievements API

    def get_character_achievements_summary(self, realm_slug, character_name):
        """
        Character Achievements API - Returns a summary of the achievements a character has completed.
        """
        resource = "profile/wow/character/{0}/{1}/achievements"
        params = [realm_slug, character_name]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    def get_character_achievements_statistics(self, realm_slug, character_name):
        """
        Character Achievements API - Returns a character's statistics as they pertain to achievements.
        """
        resource = "profile/wow/character/{0}/{1}/achievements/statistics"
        params = [realm_slug, character_name]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    # Character Appearance API

    def get_character_appearance_summary(self, realm_slug, character_name):
        """
        Character Appearance API - Returns a summary of a character's appearance settings.
        """
        resource = "profile/wow/character/{0}/{1}/appearance"
        params = [realm_slug, character_name]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    # Character Collections API

    def get_character_collection_index(self, realm_slug, character_name):
        """
        Character Collections API - Returns an index of collection types for a character.
        """
        resource = "profile/wow/character/{0}/{1}/collections"
        params = [realm_slug, character_name]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    def get_character_mount_collection_index(self, realm_slug, character_name):
        """
        Character Collections API - Returns a summary of the mounts a character has obtained.
        """
        resource = "profile/wow/character/{0}/{1}/collections/mounts"
        params = [realm_slug, character_name]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    def get_character_pet_collection_index(self, realm_slug, character_name):
        """
        Character Collections API - Returns a summary of the battle pets a character has obtained.
        """
        resource = "profile/wow/character/{0}/{1}/collections/pets"
        params = [realm_slug, character_name]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    # Character Encounters API

    def get_character_encounters_summary(self, realm_slug, character_name):
        """
        Character Encounters API - Returns a summary of a character's encounters.
        """
        resource = "profile/wow/character/{0}/{1}/encounters"
        params = [realm_slug, character_name]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    def get_character_dungeons(self, realm_slug, character_name):
        """
        Character Encounters API - Returns a summary of a character's completed dungeons.
        """
        resource = "profile/wow/character/{0}/{1}/encounters/dungeons"
        params = [realm_slug, character_name]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    def get_character_raids(self, realm_slug, character_name):
        """
        Character Encounters API - Returns a summary of a character's completed raids.
        """
        resource = "profile/wow/character/{0}/{1}/encounters/raids"
        params = [realm_slug, character_name]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    # Character Equipment API

    def get_character_equipment_summary(self, realm_slug, character_name):
        """
        Character Equipment API - Returns a summary of the items equipped by a character.
        """
        resource = "profile/wow/character/{0}/{1}/equipment"
        params = [realm_slug, character_name]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    # Character Hunter Pets API

    def get_character_hunter_pets_summary(self, realm_slug, character_name):
        """
        Character Hunter Pets API - If the character is a hunter, returns a summary of the character's hunter pets.
        """
        resource = "profile/wow/character/{0}/{1}/hunter-pets"
        params = [realm_slug, character_name]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    # Character Media API

    def get_character_media_summary(self, realm_slug, character_name):
        """
        Character Media API - Returns a summary of the media assets available for a character (such as an avatar render).
        """
        resource = "profile/wow/character/{0}/{1}/character-media"
        params = [realm_slug, character_name]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    # Character Mythic Keystone Profile API

    def get_character_mythic_keystone_profile(self, realm_slug, character_name):
        """
        Character Mythic Keystone Profile API - Returns the Mythic Keystone profile index for a character.
        """
        resource = "profile/wow/character/{0}/{1}/mythic-keystone-profile"
        params = [realm_slug, character_name]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    def get_character_mythic_keystone_profile_season(
        self, realm_slug, character_name, season_id
    ):
        """
        Character Mythic Keystone Profile API - Returns the Mythic Keystone season details for a character.
        """
        resource = "profile/wow/character/{0}/{1}/mythic-keystone-profile/season/{2}"
        params = [realm_slug, character_name, season_id]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    # Character Professions API

    def get_character_professions_summary(self, realm_slug, character_name):
        """
        Character Professions API - Returns a summary of professions for a character.
        """
        resource = "profile/wow/character/{0}/{1}/professions"
        params = [realm_slug, character_name]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    # Character Profile API

    def get_character_profile_summary(self, realm_slug, character_name):
        """
        Character Profile API - Returns a profile summary for a character.
        """
        resource = "profile/wow/character/{0}/{1}"
        params = [realm_slug, character_name]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    def get_character_profile_status(self, realm_slug, character_name):
        """
        Character Profile API - Returns the status and a unique ID for a character.
        """
        resource = "profile/wow/character/{0}/{1}/status"
        params = [realm_slug, character_name]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    # Character PvP API

    def get_character_pvp_bracket_stats(self, realm_slug, character_name, pvp_bracket):
        """
        Character PvP API - Returns the PvP bracket statistics for a character.
        """
        resource = "profile/wow/character/{0}/{1}/pvp-bracket/{2}"
        params = [realm_slug, character_name, pvp_bracket]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    def get_character_pvp_summary(self, realm_slug, character_name):
        """
        Character PvP API - Returns a PvP summary for a character.
        """
        resource = "profile/wow/character/{0}/{1}/pvp-summary"
        params = [realm_slug, character_name]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    # Character Quests API

    def get_character_quests(self, realm_slug, character_name):
        """
        Character Quests API - Returns a character's active quests as well as a link to the character's completed quests.
        """
        resource = "profile/wow/character/{0}/{1}/quests"
        params = [realm_slug, character_name]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    def get_character_completed_quests(self, realm_slug, character_name):
        """
        Character Quests API - Returns a list of quests that a character has completed.
        """
        resource = "profile/wow/character/{0}/{1}/quests/completed"
        params = [realm_slug, character_name]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    # Character Reputations API

    def get_character_reputations_summary(self, realm_slug, character_name):
        """
        Character Reputations API - Returns a summary of a character's reputations.
        """
        resource = "profile/wow/character/{0}/{1}/reputations"
        params = [realm_slug, character_name]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    # Character Specializations API

    def get_character_specializations_summary(self, realm_slug, character_name):
        """
        Character Specializations API - Returns a summary of a character's specializations.
        """
        resource = "profile/wow/character/{0}/{1}/specializations"
        params = [realm_slug, character_name]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    # Character Statistics API

    def get_character_stats_summary(self, realm_slug, character_name):
        """
        Character Statistics API - Returns a statistics summary for a character.
        """
        resource = "profile/wow/character/{0}/{1}/statistics"
        params = [realm_slug, character_name]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    # Character Titles API

    def get_character_titles_summary(self, realm_slug, character_name):
        """
        Character Titles API - Returns a summary of titles a character has obtained.
        """
        resource = "profile/wow/character/{0}/{1}/titles"
        params = [realm_slug, character_name]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    # Guild API

    def get_guild(self, realm_slug, name_slug):
        """
        Guild API - Returns a single guild by its name and realm.
        """
        resource = "data/wow/guild/{0}/{1}"
        params = [realm_slug, name_slug]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    def get_guild_activity(self, realm_slug, name_slug):
        """
        Guild API - Returns a single guild's activity by name and realm.
        """
        resource = "data/wow/guild/{0}/{1}/activity"
        params = [realm_slug, name_slug]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    def get_guild_achievements(self, realm_slug, name_slug):
        """
        Guild API - Returns a single guild's achievements by name and realm.
        """
        resource = "data/wow/guild/{0}/{1}/achievements"
        params = [realm_slug, name_slug]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)

    def get_guild_roster(self, realm_slug, name_slug):
        """
        Guild API - Returns a single guild's roster by its name and realm.
        """
        resource = "data/wow/guild/{0}/{1}/roster"
        params = [realm_slug, name_slug]
        namespace = "profile-{0}"
        return self.get_resource(resource, *params)
