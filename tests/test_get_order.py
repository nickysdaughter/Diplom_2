import allure
import requests

import urls

class TestGetOrder:
    @allure.title('Проверка получения списка заказов авторизованного поьзователя')
    def test_get_orders_authenticated_user_success(self, create_and_delete_user):
        headers = {'Authorization': create_and_delete_user[1]['accessToken']}
        response = requests.get(urls.GET_ORDER_URL, headers=headers)
        json_response = response.json()
        assert response.status_code == 200
        assert json_response['success'] is True
        assert 'orders' in json_response.keys()
        assert 'total' in json_response.keys()

    @allure.title('Проверка получения списка заказов неавторизованного пользователя')
    def test_get_orders_authenticated_user_unauthorized(self):
        response = requests.get(urls.GET_ORDER_URL)
        assert response.status_code == 401
        assert response.json() == {'success': False, 'message': 'You should be authorised'}



