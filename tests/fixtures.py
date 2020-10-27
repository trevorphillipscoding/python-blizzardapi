import pytest
import requests


def get_success_response():
    mock = requests.models.Response()
    mock.status_code = 200
    mock._content = b"{}"
    return mock


@pytest.fixture
def response_mock(mocker):
    return mocker.patch("requests.Session.get", return_value=get_success_response())
