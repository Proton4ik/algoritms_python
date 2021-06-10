from collections import namedtuple


def base_func():
    com_name = "Company"
    num_com = int(input("Введите количество компаний: "))
    companies = namedtuple(com_name, " name quart_1 quart_2 quart_3 quart_4")
    money_av = {}
    for i in range(num_com):
        company_list = companies(
            name=input("Введите название компании: "), quart_1=int(input("Введите прибыль за первый квартал: ")),
            quart_2=int(input("Введите прибыль за второй квартал: ")),
            quart_3=int(input("Введите прибыль за третий квартал: ")),
            quart_4=int(input("Введите прибыль за четвертый квартал: ")))
        money_av[company_list.name] = (company_list.quart_1 + company_list.quart_2 + company_list.quart_3 +
                                       company_list.quart_4) / 4
    all_com_av = 0
    for value in money_av.values():
        all_com_av = all_com_av + value
    all_com_av = all_com_av / num_com
    for key, value in money_av.items():
        if value > all_com_av:
            print(f"{key} - прибыль выше среднего значения")
        elif value < all_com_av:
            print(f"{key} - прибыль ниже среднего значения")
        elif value == all_com_av:
            print(f"{key} - среднее значение прибыли")


base_func()
