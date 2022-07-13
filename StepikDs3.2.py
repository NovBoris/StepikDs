# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
#
# Примечание:
# Считать все строки по одной из стандартного потока ввода вы можете, например, так
#
# import sys
#
# for line in sys.stdin:
#     line = line.rstrip()
#     # process line

# import re
# import sys

# for line in sys.stdin:
#     line = line.strip()
#     if line.count('cat') > 0:
#         print(line)
#
# # Второй вариант

# import re
# import sys

# for line in sys.stdin:
#     line = line.strip()
#     if re.search(r"cat.*cat", line):
#         print(line)

# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве слова.
#
# Примечание:
# Для работы со словами используйте группы символов \b и \B.
# Описание этих групп вы можете найти в документации.

# import re
# import sys
#
# for line in sys.stdin:
#     line = line.strip()
#     pattern = r'\bcat\b'
#     if re.search(pattern, line):
#         print(line)

# Вам дана последовательность строк.
# Выведите строки, содержащие две буквы "z", между которыми ровно три символа.

# import re
# import sys
#
# for line in sys.stdin:
#     line = line.strip()
#     if re.search(r'z.{3}z', line):
#         print(line)

# Вам дана последовательность строк.
# Выведите строки, содержащие обратный слеш "\".

# import re
# import sys
#
# for line in sys.stdin:
#     line = line.strip()
#     if re.search(r'\\', line):
#         print(line)

# Вам дана последовательность строк.
# Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).

# import re
# import sys
#
# for line in sys.stdin:
#     line = line.strip()
#     if re.search(r'\b(\w)(\1)\b', line):
#         print(line)

# Вам дана последовательность строк.
# В каждой строке замените все вхождения подстроки "human" на подстроку "computer" и выведите полученные строки.

# import re
# import sys
#
# for line in sys.stdin:
#     line = line.strip()
#     line_Fix = re.sub(r'human', r'computer', line)
#     print(line_Fix)

# Вам дана последовательность строк.
# В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a"
# (регистр не важен), на слово "argh".
#
# Примечание:
# Обратите внимание на параметр count у функции sub.

# import re
# import sys
#
# for line in sys.stdin:
#     line = line.strip()
#     line_Fix = re.sub(r'\ba+\b', r'argh', line, count=1, flags=re.IGNORECASE)
#     print(line_Fix)

# Вам дана последовательность строк.
# В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
# Буквой считается символ из группы \w.

# import re
# import sys
#
# for line in sys.stdin:
#     line = line.strip()
#     line_Fix = re.sub(r'\b(\w)(\w)(\w*)\b', r'\2\1\3', line)
#     print(line_Fix)

# Вам дана последовательность строк.
# В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
# Буквой считается символ из группы \w.

# import re
# import sys
#
# for line in sys.stdin:
#     line = line.strip()
#     line = re.sub(r'(\w)\1+', r'\1', line)
#     print(line)

# Примечание:
# Эта задача является дополнительной, то есть ее решение не принесет вам баллы.
# Задача сложнее остальных задач из этого раздела, и идея ее решения выходит за рамки
# простого понимания регулярных выражений как средства задания шаблона строки.
# Мы решили включить данную задачу в урок, чтобы показать, что регулярным выражением можно
# проверить не только "внешний вид" строки, но и заложенный в ней смысл.
#
#
# Вам дана последовательность строк.
# Выведите строки, содержащие двоичную запись числа, кратного 3.
#
# Двоичной записью числа называется его запись в двоичной системе счисления.
#
# Примечание 2:
# Данная задача очень просто может быть решена приведением строки к целому числу и проверке остатка от
# деления на три, но мы все же предлагаем вам решить ее, не используя приведение к числу.

# import re
# import sys
#
#
# def divthree(a: str) -> bool:
#     odds = sum([int(x) for x in a[::2]])
#     evens = sum([int(x) for x in a[1::2]])
#     diff = odds - evens
#     if diff/3 == diff//3:
#         return True
#     return False
#
#
# for line in sys.stdin:
#     line = line.strip()
#     if line.isdigit():
#         if divthree(line):
#             print(line)

# Решение через re

# import re
# import sys
#
# pattern = "^(0|(1(01*0)*1))*$"
# pattern = re.compile(pattern)
# for line in sys.stdin:
#     line = line.rstrip()
#     if pattern.match(line):
#         print(line)
