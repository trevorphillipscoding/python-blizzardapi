import pytest
import requests
from blizzardapi import BlizzardApi
from blizzardapi.exceptions import (
    BlizzardApiClientException,
    BlizzardApiRequestException,
)


def get_success_response():
    mock = requests.models.Response()
    mock.status_code = 200
    mock._content = b"{}"
    return mock


def get_exception_response():
    mock = requests.exceptions.RequestException()
    return mock


def get_failed_response():
    mock = requests.models.Response()
    mock.status_code = 401
    mock._content = b"{}"
    return mock


@pytest.fixture
def success_response_mock(mocker):
    return mocker.patch("requests.Session.get", return_value=get_success_response())


@pytest.fixture
def exception_response_mock(mocker):
    return mocker.patch("requests.Session.get", return_value=get_exception_response())


@pytest.fixture
def failed_response_mock(mocker):
    return mocker.patch("requests.Session.get", return_value=get_failed_response())


class TestApi:
    def setup(self):
        self.test_url = "https://example.com"
        self.params = {
            "access_token": "access_token",
            "locale": "en_US",
        }

    def test_no_tokens_api(self):
        with pytest.raises(BlizzardApiClientException):
            _ = BlizzardApi()

    def test_no_client_id_api(self):
        with pytest.raises(BlizzardApiClientException):
            _ = BlizzardApi(client_id="client_id")

    def test_no_client_secret_api(self):
        with pytest.raises(BlizzardApiClientException):
            _ = BlizzardApi(client_secret="client_secret")

    # def test_api_with_client_tokens(self):
    #     api = BlizzardApi(client_id="client_id", client_secret="client_secret")
    #     assert isinstance(api, BlizzardApi)

    # def test_api_with_access_token(self):
    #     api = BlizzardApi(access_token="access_token")
    #     assert isinstance(api, BlizzardApi)

    # def test_request_handler_request_success(self, success_response_mock):
    #     params = self.params
    #     api = BlizzardApi(client_id="client_id", client_secret="client_secret")
    #     api._access_token = "access_token"
    #     api._request_handler(self.test_url)
    #     success_response_mock.assert_called_with(self.test_url, params=params)

    # def test_request_handler_request_exception(self, exception_response_mock):
    #     params = self.params
    #     api = BlizzardApi(client_id="client_id", client_secret="client_secret")
    #     api._access_token = "access_token"

    #     with pytest.raises(BlizzardApiRequestException):
    #         api._request_handler(self.test_url)

    # def test_request_handler_response_not_ok(self, failed_response_mock):
    #     params = self.params
    #     api = BlizzardApi(client_id="client_id", client_secret="client_secret")
    #     api._access_token = "access_token"

    #     with pytest.raises(BlizzardApiRequestException):
    #         api._request_handler(self.test_url)
