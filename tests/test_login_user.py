import allure
import helpers
from helpers import UsersAPI
from data import UserData, Message


@allure.description('Тесты на Авторизацию пользователя')
class TestLoginUser:
    @allure.title('Проверка успешной авторизации пользователя, с существующими данными')
    def test_success_auth_user_exist_data(self, authoriz_and_del_user):
        response = authoriz_and_del_user[1]
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Проверка ошибки авторизации пользователя с неверным логином')
    def test_error_auth_user_with_bad_login(self):
        data_user = helpers.generate_data_user()
        response = UsersAPI().auth_login_user(data_user)
        assert response.status_code == 401 and response.json()['message'] == Message.DATA_INCORRECT

    @allure.title('Проверка ошибки авторизации пользователя с неверным паролем')
    def test_error_auth_user_with_bad_password(self):
        response = UsersAPI().auth_login_user(UserData.USER_DATA_BAD_PAS)
        assert response.status_code == 401 and response.json()['message'] == Message.DATA_INCORRECT
