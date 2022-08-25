# num = int(input())
# while num > 0:
#     print(num % 10)
#     num = num // 10


# num = int(input())
# while num > 0:
#     print(num % 10, end='')
#     num = num // 10


# num = int(input())
# ma = 0
# mi = 10
# while num > 0:
#     if num % 10 > ma:
#         ma = num % 10
#     if num % 10 < mi:
#         mi = num % 10
#     num = num // 10
# print('Максимальная цифра равна', ma)
# print('Минимальная цифра равна', mi)


# num = int(input())
# summa = 0
# product = 1
# long = len(str(num))
# last = num // int('1' + '0' * (long - 1))
# summa_l_f = num // int('1' + '0' * (long - 1)) + (num % 10)
# while num > 0:
#     summa += num % 10
#     product *= num % 10
#     num = num // 10
# print(summa)
# print(long)
# print(product)
# print(summa / long)
# print(last)
# print(summa_l_f)


# num = int(input())
# long = len(str(num))
# print((num // int('1' + '0' * (long - 2))) % 10)


# num = int(input())
# a = num % 10
# while num > 0:
#     if num % 10 != a:
#         print('NO')
#         break
#     num = num // 10
# else:
#     print('YES')


# num = int(input())
# a = (num % 10) - 1
# while num > 0:
#     if num % 10 >= a:
#         a = num % 10
#         num = num // 10
#         continue
#     print('NO')
#     break
# else:
#     print('YES')
