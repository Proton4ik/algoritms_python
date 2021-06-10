from collections import defaultdict
from collections import deque


def dx(string):
    dex = 0
    num = deque(string)
    num.reverse()
    for i in range(len(num)):
        dex += table[num[i]] * 16 ** i
    return dex


def hx(number):
    num = deque()
    while number > 0:
        d = number % 16
        for i in table:
            if table[i] == d:
                num.append(i)
        number //= 16
    num.reverse()
    return list(num)


sym = '0123456789ABCDEF'
table = defaultdict(int)
counter = 0
for key in sym:
    table[key] += counter
    counter += 1
number_1 = dx(input('Введите первое число в шестнадцатиричном формате: ').upper())
number_2 = dx(input('Введите второе число в шестнадцатиричном формате: ').upper())
print(f'Сумма чисел: {hx(number_1 + number_2)}')
print(f'Произведение чисел: {hx(number_1 * number_2)}')
