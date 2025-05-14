import allure
import requests

import error_text
import urls
from data import TestUserUpdate

class TestUpdateUser:
    @allure.title('Проверка изменения данных пользователя с авторизацией')
    def test_update_user_data_with_auth(self, create_and_delete_user):
        response = requests.patch(urls.USER_GET_OR_UPDATE_URL, headers={
            'Authorization': create_and_delete_user[1]['accessToken']}, data=TestUserUpdate.updated_user_data)
        json_response = response.json()
        assert response.status_code == 200
        assert json_response['success'] is True
        assert json_response['user']['email'] == TestUserUpdate.updated_user_data['email']
        assert json_response['user']['name'] == TestUserUpdate.updated_user_data['name']

    @allure.title('Проверка изменения данных пользователя без авторизации')
    def test_update_user_data_without_auth(self):
        new_data = {
            'email': 'testUser@test.com',
            'name': 'TestUser'
        }
        response = requests.patch(urls.USER_GET_OR_UPDATE_URL, data=new_data)
        assert response.status_code == 401 and response.json() == {'success': False,
                                                                   'message': error_text.ERR_WITHOUT_AUTH}

