import pytest
import requests


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
