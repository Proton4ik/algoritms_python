"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""
users_list = {"fhfhhgh1":{ "password": 88888, "activated": True},
              "fhfhhgh2":{ "password": 88888, "activated": True},
              "fhfhhgh3":{ "password": 88888, "activated": True}}



# O(1)-этот лучше
def login_ver_1(users_list, username, password):
        if users_list.get(username):
            if users_list[username]["password"] == password and users_list[username]["activated"]:
                return print ("Вход выполнен")
            elif users_list[username]["password"] == password and not users_list[username]["activated"]:
                return print("Учетная запись не активирована")
            elif users_list[username]["password"] != password:
                return print("Неверный пароль")
        else:
           return print("Пользователя не существует")

# O(n)
def login_ver_2(users_list, username, password):
    for key, value in users_list.items():
        if key == username:
            if value["password"] == password and value["activated"]:
                return print ("Вход выполнен")
            elif value["password"] == password and not value["activated"]:
                return print("Учетная запись не активирована")
            elif value["password"] != password:
                return print("Неверный пароль")
        else:
           return print("Пользователя не существует")


#a = users_list.get("fhfhhgh1")
#print(a)
login_ver_2(users_list, "fhfhhgh1", 88888)
login_ver_1(users_list, "fhfhhgh1", 88888)
