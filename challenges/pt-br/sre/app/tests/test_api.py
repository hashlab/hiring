import os
from unittest import mock

import pytest
from flask import url_for


@pytest.fixture
def access_counter_url():
    return url_for("access_counter")


@pytest.fixture
def authorization_header():
    return {"Authorization": "Token foobar"}


def test_access_counter_unauthorized(client, access_counter_url):
    response = client.get(access_counter_url)
    
    assert response.status_code == 401


@mock.patch.dict(os.environ, {"AUTH_TOKEN": "foobar"})
def test_access_counter(client, access_counter_url, authorization_header):
    response = client.get(access_counter_url, headers=authorization_header)

    assert response.status_code == 200


@mock.patch.dict(os.environ, {"AUTH_TOKEN": "foobar"})
@mock.patch("app.utils.redis_client.get")
def test_access_counter_no_key(mock_redis_get, client, access_counter_url, authorization_header):
    mock_redis_get.return_value = None
    response = client.get(access_counter_url, headers=authorization_header)

    assert response.status_code == 200
    assert response.json["access_counter"] == 1


@mock.patch.dict(os.environ, {"AUTH_TOKEN": "foobar"})
@mock.patch("app.utils.redis_client.get")
def test_access_counter_with_key(mock_redis_get, client, access_counter_url, authorization_header):
    mock_redis_get.return_value = 12
    response = client.get(access_counter_url, headers=authorization_header)

    assert response.status_code == 200
    assert response.json["access_counter"] == 13
