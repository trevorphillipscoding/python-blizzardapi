# python-blizzardapi
![Python package](https://github.com/trevorphillips/python-blizzardapi/workflows/Python%20package/badge.svg) [![codecov](https://codecov.io/gh/trevorphillips/python-blizzardapi/branch/main/graph/badge.svg?token=67MW8UHAG1)](https://codecov.io/gh/trevorphillips/python-blizzardapi) ![GitHub](https://img.shields.io/github/license/trevorphillips/python-blizzardapi) ![PyPI](https://img.shields.io/pypi/v/python-blizzardapi) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-blizzardapi)

python-blizzardapi is a client library for Blizzard's APIs.

Current supported features include:
- Battle.net User
- WoW Profile
- WoW Game Data
- Diablo 3 Community
- Diablo 3 Game Data

To gain access to Blizzard's API please register [here](https://develop.battle.net/access/) to obtain a client id and client secret.

For more information on Blizzard's API visit:

[Official Documentation](https://develop.battle.net/documentation)  
[Official API Forum](https://us.forums.blizzard.com/en/blizzard/c/api-discussion)

# Requirements

Python (3.6, 3.7, 3.8, 3.9)

# Installing

`pip install python-blizzardapi`
    
# Example

**main.py**
```python
from blizzardapi import BlizzardApi

api_client = BlizzardApi("client_id", "client_secret")

# Unprotected API endpoint
categories_index = api_client.wow.game_data.get_achievement_categories_index("us", "en_US")

# Protected API Endpoint
summary = api_client.wow.profile.get_account_profile_summary("us", "en_US", "access_token")
```

# Access token vs Client ID/Client Secret

You can pass in a `client_id` and `client_secret` and use almost any endpoint except for a few that require an `access_token` obtained via OAuth authorization code flow. You can find more information at https://develop.battle.net/documentation/guides/using-oauth/authorization-code-flow.

Here is the list of endpoints, specified by Blizzard, that require an OAuth token.

```
GET /oauth/userinfo
GET /profile/user/wow
GET /profile/user/wow/protected-character/{realm-id}-{character-id}
GET /profile/user/wow/collections
GET /profile/user/wow/collections/pets
GET /profile/user/wow/collections/mounts
```
