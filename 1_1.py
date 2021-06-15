import time
from memory_profiler import profile
import itertools


# Имитация светофора
# Вариант 1
class TrafficLight:

    __color = "pulse yellow"

    @profile
    def running(self):
        while True:
            self.__color = "red"
            if self.__color != "red":
                print("Ошибка в работе светофора. Мигающий Желтый!")
                self.__color = "pulse yellow"
                print(self.__color)
                break
            print("Красный! Будет гореть 7 секунд")
            print(self.__color)
            time.sleep(7)
            self.__color = "yellow"
            if self.__color != "yellow":
                print("Ошибка в работе светофора. Мигающий Желтый!")
                self.__color = "pulse yellow"
                print(self.__color)
                break
            print("Желтый! Будет гореть 2 секунды")
            print(self.__color)
            time.sleep(2)
            self.__color = "green"
            if self.__color != "green":
                print("Ошибка в работе светофора. Мигающий Желтый!")
                self.__color = "pulse yellow"
                print(self.__color)
                break
            print("Зеленый! Будет гореть 5 секунд")
            print(self.__color)
            time.sleep(5)
            working = input("Если хотите выключить светофор введите q: ")
            if working == "q":
                print("Мигает Желтый!")
                self.__color = "pulse yellow"
                print(self.__color)
                break


light_switcher = TrafficLight()
light_switcher.running()
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     12     19.8 MiB     19.8 MiB           1       @profile
#     13                                             def running(self):
#     14                                                 while True:
#     15     19.8 MiB      0.0 MiB           1               self.__color = "red"
#     16     19.8 MiB      0.0 MiB           1               if self.__color != "red":
#     17                                                         print("Ошибка в работе светофора. Мигающий Желтый!")
#     18                                                         self.__color = "pulse yellow"
#     19                                                         print(self.__color)
#     20                                                         break
#     21     19.8 MiB      0.0 MiB           1               print("Красный! Будет гореть 7 секунд")
#     22     19.8 MiB      0.0 MiB           1               print(self.__color)
#     23     19.8 MiB      0.0 MiB           1               time.sleep(7)
#     24     19.8 MiB      0.0 MiB           1               self.__color = "yellow"
#     25     19.8 MiB      0.0 MiB           1               if self.__color != "yellow":
#     26                                                         print("Ошибка в работе светофора. Мигающий Желтый!")
#     27                                                         self.__color = "pulse yellow"
#     28                                                         print(self.__color)
#     29                                                         break
#     30     19.8 MiB      0.0 MiB           1               print("Желтый! Будет гореть 2 секунды")
#     31     19.8 MiB      0.0 MiB           1               print(self.__color)
#     32     19.8 MiB      0.0 MiB           1               time.sleep(2)
#     33     19.8 MiB      0.0 MiB           1               self.__color = "green"
#     34     19.8 MiB      0.0 MiB           1               if self.__color != "green":
#     35                                                         print("Ошибка в работе светофора. Мигающий Желтый!")
#     36                                                         self.__color = "pulse yellow"
#     37                                                         print(self.__color)
#     38                                                         break
#     39     19.8 MiB      0.0 MiB           1               print("Зеленый! Будет гореть 5 секунд")
#     40     19.8 MiB      0.0 MiB           1               print(self.__color)
#     41     19.8 MiB      0.0 MiB           1               time.sleep(5)
#     42     19.8 MiB      0.0 MiB           1               working = input("Если хотите выключить светофор введите q: ")
#     43     19.8 MiB      0.0 MiB           1               if working == "q":
#     44     19.8 MiB      0.0 MiB           1                   print("Мигает Желтый!")
#     45     19.8 MiB      0.0 MiB           1                   self.__color = "pulse yellow"
#     46     19.8 MiB      0.0 MiB           1                   print(self.__color)
#     47     19.8 MiB      0.0 MiB           1                   break


# Вариант 2
class TrafficLight1:
    __color = [['red', [7, 31]], ['yellow', [2, 33]], ['green', [5, 32]], ['yellow', [2, 33]]]

    @profile
    def running(self):
        i = 0
        for light in itertools.cycle(self.__color):
            print(f'\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m', end='')
            time.sleep(light[1][0])
            i += 1
            if i == 3:
                break


t1 = TrafficLight1()
t1.running()
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#   58     19.8 MiB     19.8 MiB           1       @profile
#   59                                             def running(self):
#   60     19.8 MiB      0.0 MiB           1           i = 0
#   61     19.8 MiB      0.0 MiB           3           for light in itertools.cycle(self.__color):
#   62     19.8 MiB      0.0 MiB           3               print(f'\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m', end='')
#   64     19.9 MiB      0.0 MiB           3               i += 1
#   66     19.9 MiB      0.0 MiB           1                   break
# В обоих решения нет инкрементов, но во втором варианте память на линии 64 увеличилась- баг profilera.
# В целом при прочих равных второй вариант предпочтительнее
