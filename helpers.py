import allure
import requests
import secrets
import random
import string
from data import URLs


def generate_random_string(length):
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step('Генерация логина, пароля, имени')
def generate_data_user():
    email = f'{generate_random_string(10)}@yandex.ru'
    password = generate_random_string(10)
    name = generate_random_string(10)
    data_user = {
        'email': email,
        'password': password,
        'name': name
    }
    return data_user


@allure.step('Генерация неверного хэша ингредиентов')
def generate_hash_16():
    hex = secrets.token_hex(16)
    return hex

class UsersAPI:
    def __init__(self):
        self.main_url = URLs.MAIN_URL
        self.url_user_create = f'{URLs.MAIN_URL}{URLs.ENDPOINT_USER_CREATE}'
        self.url_user_login = f'{URLs.MAIN_URL}{URLs.ENDPOINT_USER_LOGIN}'
        self.url_user_update = f'{URLs.MAIN_URL}{URLs.ENDPOINT_USER_UPDATE}'
        self.url_user_delete = f'{URLs.MAIN_URL}{URLs.ENDPOINT_USER_DELETE}'

    @allure.step('Создание пользователя')
    def create_new_user(self, payload):
        response = requests.post(self.url_user_create, data=payload)
        return response

    @allure.step('Авторизация пользователя')
    def auth_login_user(self, payload):
        response = requests.post(self.url_user_login, data=payload)
        return response

    @allure.step('Обновление данных пользователя')
    def update_data_user(self, token_user, payload):
        headers = {"Authorization": token_user}
        response = requests.patch(self.url_user_update, headers=headers, data=payload)
        return response

    @allure.step('Удаление пользователя')
    def delete_user(self, token_user):
        headers = {"Authorization": token_user}
        response = requests.delete(self.url_user_delete, headers=headers)
        return response

class OrdersAPI:
    def __init__(self):
        self.main_url = URLs.MAIN_URL
        self.url_order = f'{URLs.MAIN_URL}{URLs.ENDPOINT_ORDER_CREATE}'

    @allure.step('Создание нового заказа')
    def create_new_order(self, token_user, ingredients_data):
        headers = {'Authorization': token_user}
        payload = {'ingredients': ingredients_data}
        response = requests.post(self.url_order, headers=headers, json=payload)
        return response

    @allure.step('Получение заказов пользователя')
    def get_orders_user(self, token_user):
        headers = {"Authorization": token_user}
        response = requests.get(self.url_order, headers=headers)
        return response