from timeit import timeit


array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


print(func_1())
print(func_2())
print(timeit("func_1()", globals=globals()))
print(timeit("func_2()", globals=globals()))


def my_func():
    my_num = max(array, key=array.count)
    return f'Чаще всего встречается число {my_num}, ' \
           f'оно появилось в массиве {array.count(my_num)} раз(а)'


print(my_func())
print(timeit("my_func()", globals=globals()))
# Оптималный вариант с функцией max и ключом. Он выигрывает у остальных по сложности так и по количеству кода. Из
# начальных двух быстрее первая в связи с меньшей сложностью.
