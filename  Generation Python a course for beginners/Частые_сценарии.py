# a, b = int(input()), int(input())
# count = 0
# for i in range(a, b + 1):
#     if (i ** 3) % 10 == 4 or (i ** 3) % 10 == 9:
#         count += 1
# print(count)


# n = int(input())
# summa = 0
# for i in range(n):
#     summa += int(input())
# print(summa)


# from math import log
# n = int(input())
# res = 1
# for i in range(2, n + 1):
#     res += 1 / i
# print(res - log(n))


# n = int(input())
# res = 0
# for i in range(1, n + 1):
#     if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8:
#         res += i
# print(res)


# n = int(input())
# res = 1
# for i in range(2, n + 1):
#     res *= i
# print(res)


# res = 1
# for _ in range(10):
#     n = int(input())
#     if n > 0:
#         res *= n
# print(res)


# res = 0
# n = int(input())
# for i in range(1, n + 1):
#     if n % i == 0:
#         res += i
# print(res)


# n = int(input())
# res = 0
# for i in range(1, n + 1):
#     res += ((-1) ** (i + 1)) * i
# print(res)


# n = int(input())
# a = 0
# b = 0
# for i in range(n):
#     number = int(input())
#     if number > b:
#         a = b
#         b = number
#     elif number > a:
#         a = number
#     print(a, b)
# print(b)
# print(a)


# for _ in range(10):
#     n = int(input())
#     if n % 2 != 0:
#         print('NO')
#         break
# else:
#     print('YES')

# fib1 = 1
# fib2 = 1
# for i in range(int(input())):
#     print(fib1, end=' ')
#     fib1, fib2 = fib2, fib1 + fib2
