import blizzardapi

api = blizzardapi.WowApi(client_id="c1ff84fe7c454bfa95b14be844ae29f8",
                         client_secret="YBTMPRlOd8O6yWGRaad8sPv1E1dP6lam")

test = api.game_data.get_achievements_index()
print(test)
