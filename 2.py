#a = 123//10
#print(a)

i = 0
j = 0



def how_many(num):
    global i
    global j
    if num == 0 and i == 0 and j == 0:
        return print ("Вы ввели 0")
    elif (num == 0 and i != 0) or (num == 0 and j != 0):
        return print (f"В вашем числе {i} четных и {j} нечетных цифр.")
    elif num != 0:
        if num % 2 == 0:
            i += 1
            num = num // 10
            return how_many(num)
        elif num % 2 != 0:
            j += 1
            num = num // 10
            return how_many(num)

try:
    number = int(input("Введите целое число: "))
except ValueError:
    print ("Вы ввели не число.")
    number = int(input("Введите целое число: "))
how_many(number)


