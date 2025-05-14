import pytest
import requests

import helpers
import urls


@pytest.fixture
def create_and_delete_user():
    payload = {
        'email': helpers.generate_random_email(),
        'password': helpers.generate_random_password(),
        'name': helpers.generate_random_username()
    }
    response = requests.post(urls.REGISTER_URL, data=payload)
    response_body = response.json()

    yield payload, response_body

    access_token = response_body['accessToken']
    requests.delete(urls.AUTH_URL, headers={'Authorization': access_token})