class URLs:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site'
    ENDPOINT_USER_CREATE = '/api/auth/register'
    ENDPOINT_USER_LOGIN = '/api/auth/login'
    ENDPOINT_USER_UPDATE = '/api/auth/user'
    ENDPOINT_USER_DELETE = '/api/auth/user'
    ENDPOINT_ORDER_CREATE = '/api/orders'

class Message:
    USER_EXISTS = 'User already exists'
    REQUIRED_FIELDS = 'Email, password and name are required fields'
    DATA_INCORRECT = 'email or password are incorrect'
    SHOULD_AUTH = "You should be authorised"
    BAD_INGREDIENT = "Ingredient ids must be provided"

class UserData:
    TRUE_USER_DATA = {'email': 'but6@yandex.ru',
                      'password': '456978',
                      'name': 'Марина'}

    USER_DATA_BAD_PAS = {'email': 'but6@yandex.ru',
                         'password': '45978',
                         'name': 'Марина'}

class DataOrder:
    ingredient = "61c0c5a71d1f82001bdaaa6c"