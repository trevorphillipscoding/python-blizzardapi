# python-blizzardapi

python-blizzardapi is a client library for Blizzard's APIs.

Current supported features include:
- WoW Profile
- WoW Game Data

To gain access to Blizzard's API please register [here](https://develop.battle.net/access/) to obtain a client id and client secret.

For more information on Blizzard's API visit:

[Official Documentation](https://develop.battle.net/documentation)  
[Official API Forum](https://us.forums.blizzard.com/en/blizzard/c/api-discussion)

# Requirements

Python (3.6, 3.7, 3.8, 3.9)

# Installing

` pip install python-blizzardapi`
    
# Example

**main.py**
```python
from blizzardapi import BlizzardApi

# Using only `client_id` and `client_secret`.
api_client = BlizzardApi(client_id="client_id", client_secret="client_secret")

# Using only "access_token".
api_client = BlizzardApi(access_token="access_token")

# Using different regions and locales.
api_client = BlizzardApi(access_token="access_token", region="eu", locale="de_DE")

categories_index = api_client.get_achievement_categories_index()
print(categories_index)
```

# Access token vs Client ID/Client Secret

You can pass in a `client_id` and `client_secret` and use almost any endpoint normally except for a few that require an `access_token` obtained via OAuth authorization code flow.

Here is the list of endpoints, specified by blizzard, that require an OAuth token.

```
GET /oauth/userinfo
GET /profile/user/wow
GET /profile/user/wow/protected-character/{realm-id}-{character-id}
GET /profile/user/wow/collections
GET /profile/user/wow/collections/pets
GET /profile/user/wow/collections/mounts
```

**However**, you do **NOT** need an OAuth token if you're only going to be using those endpoints for **YOUR** own character information. You only require an access token if you are using these endpoints to gain access to other people's character information.

# Todo

- Support search endpoints.
- Support other API's besides WoW.
- Support classic namespace for WoW API.
- Complete full coverage and testing.
