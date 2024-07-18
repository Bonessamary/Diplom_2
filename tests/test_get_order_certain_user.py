import allure
from helpers import UsersAPI, OrdersAPI
from data import UserData, Message


@allure.description('Тесты на получение заказов конкретного пользователя')
class TestsGetOrderCertainUser:
    @allure.title('Проверка получения заказов авторизованного пользователя')
    def test_get_orders_auth_user(self):
        auth_response = UsersAPI().auth_login_user(UserData.TRUE_USER_DATA)
        token_user = auth_response.json().get('accessToken', '')
        get_response = OrdersAPI().get_orders_user(token_user)
        assert get_response.status_code == 200 and get_response.json()['success'] is True

    @allure.title('Проверка получения заказов неавторизованного пользователя')
    def test_get_orders_not_auth_user(self):
        token_user = 'None'
        get_response = OrdersAPI().get_orders_user(token_user)
        assert get_response.status_code == 401 and get_response.json().get('message') == Message.SHOULD_AUTH