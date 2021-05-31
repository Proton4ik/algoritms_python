count = int(input("Введите количество чисел: "))
i = 0
first_el = 1
all_sum = 0


def calc(num):
    global first_el
    global all_sum
    global i
    if i == num:
        return print (f"Сумма всех элементов равна {all_sum}")
    elif i == 0 and i !=num:
        i += 1
        all_sum = first_el
        return calc(num)
    elif i < num:
        i += 1
        all_sum = all_sum + (first_el / 2 * -1)
        first_el = first_el / 2 * -1
        return calc(num)

calc(count)
