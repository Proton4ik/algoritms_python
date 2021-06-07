from timeit import timeit
from cProfile import run


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


number = 549236
print("Рекурсия", timeit("revers_1(number)", globals=globals()))
print("Цикл", timeit("revers_2(number)", globals=globals()))
print("Срез", timeit("revers_3(number)", globals=globals()))
run("revers_1(number)")
run("revers_2(number)")
run("revers_3(number)")

# судя по времени-срез самый быстрый, потом цикл, самая медленная-рекурсия. Предположительно-это из-за отсутствия
# вычислений в коде среза.


def my_func(n):
    n = str(n)
    n_list = list(n)
    n_list.reverse()
    n_rev = "".join(n_list)


print(timeit("my_func(number)", globals=globals()))
run("my_func(number)")
# Мой вариант на втором месте по скорости
