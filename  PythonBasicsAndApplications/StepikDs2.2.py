# В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
# Во второй строке дано одно число days -- число дней.
# Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней,
# равное days.
# Примечание:
# Для решения этой задачи используйте стандартный модуль datetime.
# Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta для прибавления дней к дате.

# from datetime import date, timedelta
# a, b, c = input().split()
# date_1 = date(int(a), int(b), int(c))
# b = int(input())
# bb = timedelta(b)
# res = date_1 + bb
# print(res.year, res.month, res.day)


# Алиса владеет интересной информацией, которую хочет заполучить Боб.
# Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
# У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.
#
# Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями,
# но он не смог понять какой из паролей ему нужен. Помогите ему решить эту проблему.
#
# Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
# Она представила информацию в виде строки,
# и затем записала в бинарный файл результат работы метода simplecrypt.encrypt.
#
# Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать,
# какой из паролей служит ключом для расшифровки файла с интересной информацией.
#
# Ответом для данной задачи служит расшифрованная интересная информация Алисы.
#
# Файл с информацией
# Файл с паролями

import simplecrypt
# import urllib.request as urllib
#
# passwords = urllib.urlopen('https://stepik.org/media/attachments/lesson/24466/passwords.txt')
#
# with open('encrypted.bin', 'rb') as inp:
#     encrypted = inp.read()
#
# for password in passwords:
#     password = password[:-1]
#     try:
#         print(simplecrypt.decrypt(password, encrypted).decode('utf8'))
#     except simplecrypt.DecryptionException:
#         print(password, 'is wrong')
#     else:
#         print(password, 'is correct')
#         break
