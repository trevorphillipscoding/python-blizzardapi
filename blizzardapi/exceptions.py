class BlizzardApiException(Exception):
    pass


class BlizzardApiClientException(BlizzardApiException):
    pass


class BlizzardApiOAuthException(BlizzardApiException):
    pass


class BlizzardApiRequestException(BlizzardApiException):
    pass
