from ..api import Api


class Diablo3CommunityApi(Api):
    """All Community API methods"""

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)

    # D3 Act API

    def get_act_index(self, region, locale):
        """
        D3 Act API - Returns an index of acts.
        """
        resource = "/d3/data/act"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_act(self, region, locale, act_id):
        """
        D3 Act API - Returns a single act by ID.
        """
        resource = f"/d3/data/act/{act_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    # D3 Artisan and Recipe API

    def get_artisan(self, region, locale, artisan_slug):
        """
        D3 Artisan and Recipe API - Returns a single artisan by slug.
        """
        resource = f"/d3/data/artisan/{artisan_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_recipe(self, region, locale, artisan_slug, recipe_slug):
        """
        D3 Artisan and Recipe API - Returns a single recipe by slug for the
        specified artisan.
        """
        resource = f"/d3/data/artisan/{artisan_slug}/recipe/{recipe_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    # D3 Follower API

    def get_follower(self, region, locale, follower_slug):
        """
        D3 Follower API - Returns a single follower by slug.
        """
        resource = f"/d3/data/follower/{follower_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    # D3 Character Class and Skill API

    def get_character_class(self, region, locale, class_slug):
        """
        D3 Character Class and Skill API - Returns a single character class by
        slug.
        """
        resource = f"/d3/data/hero/{class_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_api_skill(self, region, locale, class_slug, skill_slug):
        """
        D3 Character Class and Skill API - Returns a single skill by slug for a
        specific character class.
        """
        resource = f"/d3/data/hero/{class_slug}/skill/{skill_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    # D3 Item Type API

    def get_item_type_index(self, region, locale):
        """
        D3 Item Type API - Returns an index of item types.
        """
        resource = "/d3/data/item-type"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_item_type(self, region, locale, item_type_slug):
        """
        D3 Item Type API - Returns a single item type by slug.
        """
        resource = f"/d3/data/item-type/{item_type_slug}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    # D3 Item API

    def get_item(self, region, locale, item_slug_id):
        """
        D3 Item API - Returns a single item by item slug and ID.
        """
        resource = f"/d3/data/item/{item_slug_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    # D3 Profile API

    def get_api_account(self, region, locale, account_id):
        """
        D3 Profile API - Returns the specified account profile.
        """
        resource = f"/d3/profile/{account_id}/"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_api_hero(self, region, locale, account_id, hero_id):
        """
        D3 Profile API - Returns a single hero.
        """
        resource = f"/d3/profile/{account_id}/hero/{hero_id}"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_api_detailed_hero_items(self, region, locale, account_id, hero_id):
        """
        D3 Profile API - Returns a list of items for the specified hero.
        """
        resource = f"/d3/profile/{account_id}/hero/{hero_id}/items"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)

    def get_api_detailed_follower_items(
        self, region, locale, account_id, hero_id
    ):
        """
        D3 Profile API - Returns a single item by item slug and ID.
        """
        resource = f"/d3/profile/{account_id}/hero/{hero_id}/follower-items"
        query_params = {"locale": locale}
        return super().get_resource(resource, region, query_params)
