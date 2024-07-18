Задание 2: API
Тестирование ручек API для Stellar Burgers.

1.test_create_user.py - Создание пользователя:
    test_success_create_uniq_user - создать уникального пользователя;
    test_error_create_exists_user - создать пользователя, который уже зарегистрирован;
    test_error_create_user_with_empty_fields - создать пользователя и не заполнить одно из обязательных полей.
2.test_login_user.py - Логин пользователя:
    test_success_auth_user_exist_data - логин под существующим пользователем,
    test_error_auth_user_with_bad_login - логин с неверным логином,
    test_error_auth_user_with_bad_password- логин с неверным паролем.
3.test_change_data_user.py - Изменение данных пользователя:
    test_change_data_auth_user - с авторизацией,
    test_change_data_not_auth_user - без авторизации.
4.test_create_order.py - Создание заказа:
    test_create_order_auth_and_ingredients - с авторизацией,
    test_create_order_not_auth - без авторизации,
    test_create_order_auth_and_ingredients - с ингредиентами,
    test_create_order_not_ingredients - без ингредиентов,
    test_create_order_invalid_hash - с неверным хешем ингредиентов.
5.test_get_order_certain_user.py - Получение заказов конкретного пользователя:
    test_get_orders_auth_user - авторизованный пользователь,
    test_get_orders_not_auth_user - неавторизованный пользователь.