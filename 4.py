from collections import OrderedDict
from timeit import timeit


n = 1000
my_dict = {'a': 1, 'b': 2}
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
new_d = OrderedDict(sorted(d.items()))


def up_dict(dc):
    for i in range(n):
        dc.update({i: i})
    return dc


def up_od(od):
    for i in range(n):
        od.update({i: i})
    return od


print(timeit('up_dict(my_dict)', globals=globals(), number=1000))  # 0.21009059999999996
print(timeit('up_od(new_d)', globals=globals(), number=1000))      # 0.3917162

# Обычный словарь немного быстрее, и как я понял из разных ресурсов во всех операциях. Из-за этого orderdict используют
# лишь для специфических операций типа move_to_end итд.
