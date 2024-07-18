import allure
import pytest
from data import Message
import helpers
from helpers import UsersAPI


@allure.description('Тесты на cоздание пользователя')
class TestCreateUser:
    @allure.title('Проверка на успешное создание уникального пользователя')
    def test_success_create_uniq_user(self, create_data_user_and_go, delete_user):
        response = create_data_user_and_go[1]
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Проверка ошибки при создании уже зарегистрированного пользователя')
    def test_error_create_exists_user(self, create_data_user_and_go):
        user_data = create_data_user_and_go[0]
        response = UsersAPI().create_new_user(user_data)
        assert response.status_code == 403 and response.json()['message'] == Message.USER_EXISTS

    @allure.title('Проверка ошибки при создании пользователя, если не заполнено одно из обязательных полей')
    @pytest.mark.parametrize('param', ['email', 'password', 'name'])
    def test_error_create_user_with_empty_fields(self, param):
        user_data = helpers.generate_data_user()
        user_data.pop(param)
        response = UsersAPI().create_new_user(user_data)
        assert response.status_code == 403 and response.json()['message'] == Message.REQUIRED_FIELDS