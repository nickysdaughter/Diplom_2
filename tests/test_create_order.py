import allure
import requests

import urls
from data import IngredientData

class TestCreateOrder:
    @allure.title('Проверка создания заказа авторизованным пользователем')
    def test_create_order_with_auth_success(self, create_and_delete_user):
        headers = {'Authorization': create_and_delete_user[1]['accessToken']}
        payload = {'ingredients': [IngredientData.burger]}
        response = requests.post(urls.CREATE_ORDER_URL, data=payload, headers=headers)
        json_response = response.json()
        assert response.status_code == 200
        assert json_response['success'] is True
        assert 'name' in json_response.keys()
        assert 'number' in json_response['order'].keys()

    @allure.title('Проверка создания заказа неавторизованным пользователем')
    def test_create_order_without_auth_success(self):
        payload = {'ingredients': [IngredientData.burger]}
        response = requests.post(urls.CREATE_ORDER_URL, data=payload)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Проверка создания заказа без ингредиентов')
    def test_create_order_without_ingredients_bad_request(self, create_and_delete_user):
        headers = {'Authorization': create_and_delete_user[1]['accessToken']}
        payload = {'ingredients': []}
        response = requests.post(urls.CREATE_ORDER_URL, data=payload, headers=headers)
        assert response.status_code == 400
        assert response.json() == {'success': False, 'message': 'Ingredient ids must be provided'}

    @allure.title('Проверка создания заказа с неверным хешем ингредиентов')
    def test_create_order_with_invalid_ingredient_hash_error(self, create_and_delete_user):
        headers = {'Authorization': create_and_delete_user[1]['accessToken']}
        payload = {'ingredients': [IngredientData.invalid_hash_ingredient]}
        response = requests.post(urls.CREATE_ORDER_URL, data=payload, headers=headers)
        assert response.status_code == 500
        assert response.json() == {'success': False, 'message': 'One or more ids provided are incorrect'}





