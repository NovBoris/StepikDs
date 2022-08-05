# Последние задачи.Графики.Массивы.


#В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики: они говорили каким-то странным набором звуков.

# В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении подстановочный шифр, т.е. заменяли каждый символ исходного сообщения на соответствующий ему другой символ. Биологи раздобыли ключ к шифру и теперь нуждаются в помощи:
#
# Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.
#
# Пусть, например, на вход программе передано:
# abcd
# *d%#
# abacabadaba
# #*%*d*%
#
# Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
# Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки, которые и передаём на вывод программы:
# *d*%*d*#*d*
# dacabac

# dict_1 = dict(zip((input()), (input())))
# res = ''
# for i in input():
#     for a, b in dict_1.items():
#         if i == a:
#             res += b
# print(res)
# res = ''
# for i in input():
#     for a, b in dict_1.items():
#         if i == b:
#             res += a
# print(res)

# Короткое решение

# a,b,c,d=input(),input(),input(),input()
# print(''.join(b[a.index(i)] for i in c))
# print(''.join(a[b.index(i)] for i in d))
#
# Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
# Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
#
# Попробуем написать подобную систему.
#
# На вход программе первой строкой передаётся количество dd известных нам слов, после чего на dd строках указываются эти слова. Затем передаётся количество ll строк текста для проверки, после чего ll строк текста.
#
# Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

# a = int(input())
# words = []
# while a != 0:
#     words.append(input().lower())
#     a -= 1
# b = int(input())
# res = []
# while b != 0:
#     line = input().lower().split()
#     for i in line:
#         if i not in words and i not in res:
#             res.append(i)
#     b -= 1
# for i in res:
#     print(i)

# Короткое решение

# dic = {input().lower() for i in range(int(input()))}
#
# wrd = set()
# for w in range(int(input())):
#     wrd |= {i.lower() for i in input().split()}
#
# print(*wrd.difference(dic), sep="\n")

# Группа биологов в институте биоинформатики завела себе черепашку.
#
# После дрессировки черепашка научилась понимать и запоминать указания биологов следующего вида:
# север 10
# запад 20
# юг 30
# восток 40
# где первое слово — это направление, в котором должна двигаться черепашка, а число после слова — это положительное расстояние в сантиметрах, которое должна пройти черепашка.
#
# Но команды даются быстро, а черепашка ползёт медленно, и программисты догадались, что можно написать программу, которая определит, куда в итоге биологи приведут черепашку. Для этого программисты просят вас написать программу, которая выведет точку, в которой окажется черепашка после всех команд. Для простоты они решили считать, что движение начинается в точке (0, 0), и движение на восток увеличивает первую координату, а на север — вторую.

# Программе подаётся на вход число команд nn, которые нужно выполнить черепашке, после чего nn строк с самими командами. Вывести нужно два числа в одну строку: первую и вторую координату конечной точки черепашки. Все координаты целочисленные.

# res = [0, 0]
# for i in range(int(input())):
#     a, b = input().split()
#     if a == 'север':
#         res[1] += int(b)
#     if a == 'восток':
#         res[0] += int(b)
#     if a == 'юг':
#         res[1] -= int(b)
#     if a == 'запад':
#         res[0] -= int(b)
# print(*res)

# Короткое решение

# n=int(input())
# d={'север':0,'запад':0,'юг':0,'восток':0}
# for i in range(n):
#     x=input().split()
#     d[x[0]]+=int(x[1])
# print(d['восток']-d['запад'], d['север']-d['юг'])

# Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.
#
# Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.
#
# Файл состоит из набора строк, каждая из которых представляет собой три поля:
# Класс Фамилия Рост
#
# Класс обозначается только числом. Буквенные модификаторы не используются. Номер класса может быть от 1 до 11 включительно. В фамилии нет пробелов, а в качестве роста используется натуральное число, но при подсчёте среднего требуется вычислить значение в виде вещественного числа.
#
# Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов с первого по одиннадцатый). Если про какой-то класс нет информации, необходимо вывести напротив него прочерк.
#
# В качестве ответа прикрепите файл с полученными данными о среднем росте.

# dict_1 = {}
# with open('dataset_3380_5.txt') as text:
#     for line in text:
#         line = line.split()
#         if line[0] not in dict_1:
#             dict_1[line[0]] = [int(line[2])]
#         else:
#             dict_1[line[0]] += [int(line[2])]
# print(dict_1)
# with open('dataset_3380_5.txt', 'w') as text:
#     for i in range(1, 12):
#         if str(i) not in dict_1:
#             text.write(f'{i} -')
#         else:
#             text.write(f'{i} {(sum(dict_1[str(i)]) / len(dict_1[str(i)]))}\n')

from numpy import *
#
# a = array([1,2,3])
#
# print(a)
#
# print(a.ndim) # Одномерный или нет массив
#
# print(a.shape) # Количество строк и столбцов
#
# print(a.size) # Количество элементов
#
a = arange(1, 9, 1)
print(a)
#
a = linspace(0, 9, 9)
print(a)
#
a = arange(12).reshape(4,3)
print(a)

import inline as inline
import matplotlib.pyplot as plt

from pylab import *

# x = linspace(0, 5, 10)
# y = x ** 2
# print(x)
# print(y)

# figure()
# plot(x, y, 'r')
# xlabel('x')
# ylabel('y')
# title('title')
# show()

# fig = plt.figure()
#
# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
#
# axes.plot(x, y, 'r')
#
# axes.set_xlabel('x')
# axes.set_ylabel('y')
# axes.set_title('title')
# show()


# fig = plt.figure()
#
# axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
#
# axes1.plot(x, y, 'r')
# axes1.set_xlabel('x')
# axes1.set_ylabel('y')
# axes1.set_title('title')
#
# axes2.plot(y, x, 'g')
# axes2.set_xlabel('y')
# axes2.set_ylabel('x')
# axes2.set_title('title')
#
# show()


# fig, axes = plt.subplots(nrows=1, ncols=2)
#
# for ax in axes:
#     ax.plot(x, y, 'r')
#     ax.set_xlabel('x')
#     ax.set_ylabel('y')
#     ax.set_title('title')
#
# fig.tight_layout()
# show()


# fig, axes = plt.subplots(figsize=(12,3))
#
#
# axes.plot(x, y, 'r')
# axes.set_xlabel('x')
# axes.set_ylabel('y')
# axes.set_title('title')
#
# show()


# fig, ax = plt.subplots()
#
#
# ax.plot(x, x ** 2, label="y = x ** 2")
# ax.plot(x, x ** 3, label="y = x ** 3")
# ax.legend(loc=2)
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_title('title')
#
# show()


# from numpy import *
# n = random.randn(100000)
# fig, axes = plt.subplots(1, 2, figsize=(12, 4))
#
# axes[0].hist(n)
# axes[0].set_title("Default histogram")
# axes[0].set_xlim(min(n), max(n))
#
# axes[1].hist(n, cumulative=True, bins=50)
# axes[1].set_title("Cumulative default histogram")
# axes[1].set_xlim(min(n), max(n))
#
# show()