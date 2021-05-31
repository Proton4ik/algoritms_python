import random

ask = random.randint(0, 100)
count = 1


def secret():
    global count
    global ask
    ans = int(input(f"Попытка №{count}. Введите число: "))
    if ans == ask or count == 10:
        if ans == ask:
            print ("Вы угадали!")
        else:
            print (f"У Вас закончились попытки. Правильный ответ {ask}")
    else :
        if ans > ask:
            print ("Вы ввели слишком большое число")
        else:
            print ("Вы ввели слишком маленькое число")
        count += 1
        return secret()


secret()
