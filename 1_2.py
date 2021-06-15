from memory_profiler import profile


'''Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной 
первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
'''


# 1 Вариант
@profile
def func(a):
    return a.title()


print(func("abca dsd"))

'''Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     5     20.0 MiB     20.0 MiB           1   @profile
     6                                         def func(a):
     7     20.0 MiB      0.0 MiB           1       return a.title()'''


# 2 Вариант
@profile
def my_func(a):
    separate_word = a.split(' ')
    total = []
    for i in separate_word:
        string_element = str(i)
        first_letter = string_element[:1].upper()
        word = first_letter + string_element[1:]
        total.append(word)
    return total


print(my_func("hello world"))
"""Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    13     20.0 MiB     20.0 MiB           1   @profile
    14                                         def my_func(a):
    15     20.0 MiB      0.0 MiB           1       separate_word = a.split(' ')
    16     20.0 MiB      0.0 MiB           1       total = []
    17     20.0 MiB      0.0 MiB           3       for i in separate_word:
    18     20.0 MiB      0.0 MiB           2           string_element = str(i)
    19     20.0 MiB      0.0 MiB           2           first_letter = string_element[:1].upper()
    20     20.0 MiB      0.0 MiB           2           word = first_letter + string_element[1:]
    21     20.0 MiB      0.0 MiB           2           total.append(word)
    22     20.0 MiB      0.0 MiB           1       return total"""

# Инкрементов нет. Первый вариант предпочтительнее из-за простоты.
