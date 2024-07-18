import allure
import pytest

from helpers import UsersAPI
from data import Message


@allure.description('Тесты на изменение данных пользователя')
class TestChangeDataUser:
    @allure.title('Проверка изменения данных авторизованного пользователя')
    @pytest.mark.parametrize("start_value, new_value", [("name", "new_name"),
                                                                ("email", "new_email@yandex.ru"),
                                                                ("password", "new_password")])
    def test_change_data_auth_user(self, authoriz_and_del_user, start_value, new_value):
        updated_data_for_user = {start_value: new_value}
        token_user = authoriz_and_del_user[2]
        response = UsersAPI().update_data_user(token_user, updated_data_for_user)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Проверка изменения данных неавторизованного пользователя')
    @pytest.mark.parametrize("start_value, new_value", [("name", "new_name"),
                                                                ("email", "new_email@yandex.ru"),
                                                                ("password", "new_password")])
    def test_change_data_not_auth_user(self, start_value, new_value):
        updated_data_for_user = {start_value: new_value}
        token_user = 'None'
        response = UsersAPI().update_data_user(token_user, updated_data_for_user)
        assert response.status_code == 401 and response.json()['message'] == Message.SHOULD_AUTH