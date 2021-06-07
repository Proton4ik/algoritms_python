from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def new_func(nums):
    return [i for i, el in enumerate(nums) if nums[i] % 2 == 0]


my_list = [el for el in range(10000)]
print(timeit("func_1(my_list)", globals=globals(), number=1000))
print(timeit("new_func(my_list)", globals=globals(), number=1000))
# Функция enumerate работает быстрее чем итератор несмотря на одинаковую сложность алгоритма(линейная).
# Также позволяет писать меньше кода.
