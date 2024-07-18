import allure
import helpers
from helpers import UsersAPI, OrdersAPI
from data import UserData, Message, DataOrder


@allure.description('Тесты cоздания заказа')
class TestOrderCreate:
    @allure.title('Проверка создания заказа с авторизацией и ингредиентами')
    def test_create_order_auth_and_ingredients(self):
        auth_response = UsersAPI().auth_login_user(UserData.TRUE_USER_DATA)
        token_user = auth_response.json().get('accessToken', '')
        response_create = OrdersAPI().create_new_order(token_user, DataOrder.ingredient)
        assert response_create.status_code == 200 and response_create.json()['success'] is True

    @allure.title('Проверка создания заказа без авторизации')
    def test_create_order_not_auth(self):
        token_user = ''
        response_create = OrdersAPI().create_new_order(token_user, DataOrder.ingredient)
        assert response_create.status_code == 200 and response_create.json()['success'] is True

    @allure.title('Проверка создания заказа без ингредиентов')
    def test_create_order_not_ingredients(self):
        token_user = ''
        ingredients_data = ''
        response_create = OrdersAPI().create_new_order(token_user, ingredients_data)
        assert response_create.status_code == 400 and response_create.json().get('message') == Message.BAD_INGREDIENT

    @allure.title('Проверка создания заказа с неверным хешем ингредиентов')
    def test_create_order_invalid_hash(self):
        ingredients_data = helpers.generate_hash_16()
        token_user = ''
        response_create = OrdersAPI().create_new_order(token_user, ingredients_data)
        assert response_create.status_code == 500