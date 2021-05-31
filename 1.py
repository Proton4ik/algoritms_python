def calculator():
    operator = input("Введите знак операции (+-*/ или 0 для выхода): ")
    if operator == "0":
        return print("Программа завершена.")
    else:
        if operator == "+" or operator == "-" or operator == "*" or operator == "/":
            try:
                number_1 = float(input("Введите первое число: "))
                number_2 = float(input("Введите второе число: "))
                if operator == "+":
                    result = number_1 + number_2
                    print (f"Результат сложения: {result}")
                    return calculator()
                elif operator == "-":
                    result = number_1 - number_2
                    print(f"Результат вычитания: {result}")
                    return calculator()
                elif operator == "*":
                    result = number_1 * number_2
                    print(f"Результат умножения: {result}")
                    return calculator()
                elif operator == "/":
                    try:
                        result = number_1 / number_2
                    except ZeroDivisionError:
                        print ("Делить на ноль нельзя")
                    else:
                        print (f"Результат деления: {result}")
                    return calculator()
            except ValueError:
                print ("Вы ввели строку. Введите число.")
                return calculator()
        else:
            print ("Вы ввели некорректное значение. Попробуйте снова.")
            return calculator()

calculator()




