import allure
import pytest
import helpers

from helpers import UsersAPI


@allure.step('Создание данных пользователя, передача их в ручку')
@pytest.fixture
def create_data_user_and_go():
    user_data = helpers.generate_data_user()
    response = UsersAPI().create_new_user(user_data)
    yield user_data, response

@allure.step('Авторизация и получение токена пользователя')
@pytest.fixture
def authoriz_get_token_user(create_data_user_and_go):
    data_user = create_data_user_and_go[0]
    login_user_response = UsersAPI().auth_login_user(data_user)
    token_user = login_user_response.json()['accessToken']
    return token_user, login_user_response

@allure.step('Удаление пользователя после теста')
@pytest.fixture
def delete_user(authoriz_get_token_user):
    yield
    UsersAPI().delete_user(authoriz_get_token_user[0])

@allure.step('Авторизация под созданным пользователем и удаление его после теста')
@pytest.fixture
def authoriz_and_del_user(create_data_user_and_go, authoriz_get_token_user, delete_user):
    data_user = create_data_user_and_go[0]
    login_user = authoriz_get_token_user[1]
    token_user = authoriz_get_token_user[0]
    yield data_user, login_user, token_user