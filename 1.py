from time import time

my_list = []
my_dict = {}
count_op = 100000


def time_dec(func):
    def timer(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        finish = time()
        print(f"Время выполнения {func.__name__} = {finish - start}")
        return res
    return timer


@time_dec
def ins_to_lst(lst, count):
    for i in range(count):
        lst.append(i)


@time_dec
def ins_to_dct(dct, count):
    for i in range(count):
        dct[i] = i


ins_to_lst(my_list, count_op)
ins_to_dct(my_dict, count_op)
# время выполнения операций примерно одинаковое из-за одинаковой сложности O(1)


@time_dec
def del_lst(lst, count):
    for i in range(count):
        lst.pop(i)


@time_dec
def del_dct(dct, count):
    for i in range(count):
        dct.pop(i)


del_lst(my_list, 1000)
del_dct(my_dict, 1000)

# Здесь словарные функции быстрее, так как у их операций константная сложность, а у операций списка линейная
