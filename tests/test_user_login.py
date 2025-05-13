import allure
import requests

import helpers
import urls
from data import UserTestData

class TestUserLogin:
    @allure.title('Проверка логина под существующим пользователем')
    def test_login_existing_user(self, create_and_delete_user):
        payload = create_and_delete_user[0]
        response = requests.post(urls.AUTH_URL, data=payload)
        json_response = response.json()
        assert response.status_code == 200
        assert json_response['success'] is True
        assert 'accessToken' in json_response.keys()
        assert 'refreshToken' in json_response.keys()
        assert json_response['user']['email'] == create_and_delete_user[0]['email']
        assert json_response['user']['name'] == create_and_delete_user[0]['name']

    @allure.title('Проверка логина с неверным логином')
    def test_auth_with_wrong_login_expected_error(self):
        payload = {
            'email': helpers.generate_random_email(),
            'password': UserTestData.password,
        }
        response = requests.post(urls.AUTH_URL, data=payload)
        assert response.status_code == 401 and response.json() == {"success": False,
                                                                   "message": "email or password are incorrect"}

    @allure.title('Проверка логина с неверным паролем')
    def test_auth_with_wrong_passwd_expected_error(self):
        payload = {
            'email': UserTestData.email,
            'password': helpers.generate_random_password(),
        }
        response = requests.post(urls.AUTH_URL, data=payload)
        assert response.status_code == 401 and response.json() == {"success": False,
                                                                   "message": "email or password are incorrect"}


