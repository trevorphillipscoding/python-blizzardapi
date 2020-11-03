class OauthApi:
    def __init__(self):
        self.oauth_url = "https://{0}.battle.net{1}"
        self.oauth_url_cn = "https://www.battlenet.com.cn{0}"

    def format_oauth_url(self, resource, region):
        if region == "cn":
            url = self.oauth_url_cn.format(resource)
        else:
            url = self.oauth_url.format(region, resource)

        return url
