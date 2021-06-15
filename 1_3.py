from memory_profiler import profile


"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""
my_list = [3, 20, 9, 5, 1, 8, 11, 6, 15]


# Вариант с генератором
@profile
def func1():
    new_l = [el for el in my_list if el > my_list[my_list.index(el)-1]]
    return new_l


print(func1())

'''Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     8     20.0 MiB     20.0 MiB           1   @profile
     9                                         def func1():
    10     20.0 MiB      0.0 MiB          12       new_l = [el for el in my_list if el > my_list[my_list.index(el)-1]]
    11     20.0 MiB      0.0 MiB           1       return new_l'''


# Вариант с циклом
@profile
def func2():
    i = 0
    new = []
    for el in my_list:
        if el > my_list[i-1]:
            new.append(el)
        i += 1
    return new


print(func2())

'''Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    18     20.0 MiB     20.0 MiB           1   @profile
    19                                         def func2():
    20     20.0 MiB      0.0 MiB           1       i = 0
    21     20.0 MiB      0.0 MiB           1       new = []
    22     20.0 MiB      0.0 MiB          10       for el in my_list:
    23     20.0 MiB      0.0 MiB           9           if el > my_list[i-1]:
    24     20.0 MiB      0.0 MiB           4               new.append(el)
    25     20.0 MiB      0.0 MiB           9           i += 1
    26     20.0 MiB      0.0 MiB           1       return new'''

# нет инкрементов. Наверное стоит использовать генератор, хотя мне цикл больше нравится.
