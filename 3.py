from collections import deque
from timeit import timeit


n = 1000
my_deq = deque()
my_list = list()


def fill_list(lst):
    for i in range(n):
        lst.insert(0, i)
    return lst


def fill_deq(deq):
    for i in range(n):
        deq.appendleft(i)
    return deq


print(timeit('fill_list(my_list)', globals=globals(), number=100))  # 3.3515465
print(timeit('fill_deq(my_deq)', globals=globals(), number=100))    # 0.005650999999999851
