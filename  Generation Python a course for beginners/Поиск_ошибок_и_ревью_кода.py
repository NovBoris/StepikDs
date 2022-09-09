# count = 0
# p = 1
# for i in range(1, 11):
#     x = int(input())
#     if x >= 0:
#         p = p * x
#         count = count + 1
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print('NO')


# mx = 0
# s = 0
# for i in range(10):
#     x = int(input())
#     if x < 0:
#         s += x
#         if x > mx or mx == 0:
#             mx = x
# if mx != 0:
#     print(s)
#     print(mx)
# else:
#     print('NO')


# s = 0
# for i in range(7):
#     n = int(input())
#     if n % 2 == 0:
#         s += n
# print(s)


# n = int(input())
# if (n % 10) % 3 == 0:
#     max_digit = n % 10
# else:
#     max_digit = -1
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit > max_digit:
#             max_digit = digit
#     n = n // 10
# if max_digit == -1:
#     print('NO')
# else:
#     print(max_digit)


# n = int(input())
# while n > 0:
#     n //= 10
#     if n // 10 == 0:
#         break
# print(n)

