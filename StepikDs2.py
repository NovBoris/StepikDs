# fib = lambda x : 1 if x <= 2 else fib(x - 1) + fib(x - 2)
# print(fib(311))


# n = int(input())
# sum_1 = 0
# for i in range(n):
#     a = int(input())
#     sum_1 += a
# print(sum_1)


# x = [1, 2, 3]
# print(id(x))
# print(type(id([1, 2, 3])))
#
# print()
#
# x = [1, 2, 3]
# y = x
# print(y is x)
# print(y is [1, 2, 3])
#
# print()
#
# x = [1, 2, 3]
# y = x
# print(y is x)
# x.append(4)
# print(x)
# print(y)
# print()
#
# x = [1, 2, 3]
# y = x
# y.append(4)
#
# s = "123"
# t = s
# t = t + "4"
#
# print(str(x))
#
# print()
#
# z = [1, 2, 3]
# print(type(x))
# print(type(4))
# print(type(type(x)))
#
# print()

# x = 1
# objects = [1, 2, [x], [1], 3, 4, 1, 2, 321, 'abc', 'abc']
# ans = 0
# a = []
# for obj in objects:
#     if obj not in a:
#         a.append(obj)
#         ans += 1
#
# print(ans)
#
# print(set(objects))
# print(len(set(map(id, objects))))

# def function_name(argument1, argument2):
#     return argument1 + argument2
#
#
# x = function_name(4, 23)
# y = function_name(x, 123)
# print(y)

# def list_sum(lst):
#     result = 0
#     for element in lst:
#         result += element
#     return result
#
# def sum_1(a, b):
#     return  a + b
#
# y = (14, 29)
# print(sum(y))
# z = [1, 2, 3]
# print(sum(z))
#
# y = sum_1(14, 29)
# z = list_sum([1, 2, 3])
# print(y)
# print(z)

# print()

# a = []
#
# def foo(arg1, arg2):
#   a.append("foo")
#
# foo(a.append("arg1"), a.append("arg2"))
#
# print(a)

# def closest_mod_5(x):
#     if x % 5 == 0:
#         return x
#     while x % 5:
#         x += 1
#     return x
#
# x = int(input())
# print((x + 4) // 5 * 5)
# print(closest_mod_5(x))


# def sum_1(a, b):
#     return a + b
#
# a = {'sdc': 1}
#
# print(**a)

# def s(a, *vs, b=10):
#    res = a + b
#    for v in vs:
#        res += v
#    return res
#
# print(s(11, 10, 10))

# def C(n, k):
#     if k == 0:
#         return 1
#     elif k > n:
#         return 0
#     res = C(n - 1, k) + C(n - 1, k - 1)
#     return res
#
#
# n, k = map(int, input().split())
# print(C(n, k))

# n, k = map(int, input().split())
#
# sz = max(n, k) + 1
# c = [[0] * sz for _ in range(sz)]
# print(c)
# c[0][0] = 1
# for i in range(1, sz):
#     for j in range(i + 1):
#         print(c)
#         c[i][j] = c[i - 1][j] + c[i - 1][j - 1]
#
# print(c[n][k])