import allure
import pytest
import requests

import urls
from helpers import *
import data

class TestRegistration:
    @allure.title('Проверка создания уникального пользователя')
    def test_create_unique_user(self):
        payload = {
            'email': generate_random_email(),
            'password': generate_random_password(),
            'name': generate_random_username()
        }
        response = requests.post(urls.REGISTER_URL, data=payload)
        json_response = response.json()
        assert response.status_code == 200
        assert json_response['user']['email'] == payload['email']
        assert json_response['user']['name'] == payload['name']

        # удаление пользователя, созданного в результате теста
        access_token = response.json().get('accessToken')
        headers = {'Authorization': access_token}
        requests.delete(urls.AUTH_URL, headers=headers)

    @allure.title('Проверка создания уже существующего пользователя')
    def test_create_existing_user(self):
        email = generate_random_email()
        data = {
            'email': email,
            'password': 'password',
            'name': 'user'
        }
        response = requests.post(urls.REGISTER_URL, data=data)
        assert response.status_code == 200

        response = requests.post(urls.REGISTER_URL, data=data)
        assert response.status_code == 403
        assert response.json()['message'] == 'User already exists'

        # удаление пользователя, созданного в результате теста
        access_token = response.json().get('accessToken')
        headers = {'Authorization': access_token}
        requests.delete(urls.AUTH_URL, headers=headers)

    @allure.title('Проверка создания пользователя с незаполненным обязательным полем')
    @pytest.mark.parametrize('credentials', data.credentials_with_empty_field)
    def test_registration_one_required_field_is_empty_failed_submit(self, credentials):
        response = requests.post(urls.REGISTER_URL, data=credentials)
        assert (response.status_code == 403 and response.json() ==
                {'success': False, 'message': 'Email, password and name are required fields'})

