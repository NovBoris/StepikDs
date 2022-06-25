# Реализуйте класс MoneyBox, для работы с виртуальной копилкой.
#
# Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, которые можно положить в копилку.
# Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность добавлять монеты в копилку и узнавать,
# можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.
#
# Класс должен иметь следующий вид

# class MoneyBox:
#     def __init__(self, capacity=0):
#         # конструктор с аргументом – вместимость копилки
#         self.capacity = capacity
#
#     def can_add(self, v):
#         # True, если можно добавить v монет, False иначе
#         if self.capacity - v >= 0:
#             return True
#         else:
#             return False
#
#     def add(self, v):
#         # положить v монет в копилку
#         self.capacity -= v
#         return self.capacity
#
# x = MoneyBox(25)
# x.print_x()
# x.can_add(14)
# x.add(14)
# x.print_x()


# Вам дается последовательность целых чисел и вам нужно ее обработать и вывести на экран сумму первой пятерки чисел из
# этой последовательности, затем сумму второй пятерки, и т. д.
#
# Но последовательность не дается вам сразу целиком. С течением времени к вам поступают её последовательные части.
# Например, сначала первые три элемента, потом следующие шесть, потом следующие два и т. д.
#
# Реализуйте класс Buffer, который будет накапливать в себе элементы последовательности и
# выводить сумму пятерок последовательных элементов по мере их накопления.
#
# Одним из требований к классу является то, что он не должен хранить в себе больше элементов,
# чем ему действительно необходимо, т. е. он не должен хранить элементы, которые уже вошли в пятерку,
# для которой была выведена сумма.
#
# Класс должен иметь следующий вид


# class Buffer:
#     def __init__(self, buff=[]):
#         # конструктор без аргументов
#         self.buff = buff
#
#     def add(self, *a):
#         # добавить следующую часть последовательности
#
#         for i in a:
#             if len(self.buff) < 4:
#                 self.buff.append(i)
#             else:
#                 self.buff.append(i)
#                 print(sum(self.buff))
#                 self.buff.clear()
#
#     def get_current_part(self):
#         # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
#         # добавлены
#         print(self.buff)
#
#
# buf = Buffer()
# buf.add(4, 2, 3, 4, 1, 2, 4, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3, 4)
# buf.get_current_part()




# def find_parent(descendant):
#     if ancestor in parent[descendant]:
#         print('yes')
#         return
#     elif len(parent[descendant]) == 0:
#         print('no')
#         return
#     else:
#         for i in parent[descendant]:
#             find_parent(i)
#             return
#
# parent = {}
#
#
#
#
# lst_mro = [  # список введённых строк
#     'G : F',  # сначала отнаследуем от F, потом его объявим, корректный алгоритм все равно правильно обойдёт граф, независимо что было раньше: наследование или объявление
#     'A',
#     'B : A',
#     'C : A',
#     'D : B C',
#     'E : D',
#     'F : D',
#     # а теперь другая ветка наследования
#     'X',
#     'Y : X A',  # свяжем две ветки наследования для проверки, обошла ли рекурсия предков Z и предков Y в поисках A
#     'Z : X',
#     'V : Z Y',
#     'W : V',
# ]
#
# for i in lst_mro:
#     request = i.split()
#     if len(request) == 1:
#         parent[request[0]] = []
#     else:
#         parent[request[0]] = request[2:]
#
# print(parent)
#
#
# lst_q = [  # список введённых запросов
#     'A G',      # Yes   # A предок G через B/C, D, F
#     'A Z',      # No    # Y потомок A, но не Y
#     'A W',      # Yes   # A предок W через Y, V
#     'X W',      # Yes   # X предок W через Y, V
#     'X QWE',    # No    # нет такого класса QWE
#     'A X',      # No    # классы есть, но они нет родства :)
#     'X X',      # Yes   # родитель он же потомок
#     '1 1',      # No    # несуществующий класс
# ]
#
#
# for i in lst_q:
#     ancestor, descendant = i.split()
#     if ancestor in parent[descendant]:
#         print('yes')
#     else:
#         find_parent(descendant)
#
# classes = {}
#
# def add_class(classes, class_name, parents):
#     if class_name not in classes:
#         classes[class_name] = []
#     classes[class_name].extend(parents)
#     for parent in parents:
#         if parent not in classes:
#             classes[parent] = []
#
# def found_path(classes, start, end, path=[]):
#     path = path + [start]
#     if start == end:
#         return path
#     if start not in classes:
#         return None
#     for node in classes[start]:
#         if node not in path:
#             newpath = found_path(classes, node, end, path)
#             if newpath: return newpath
#     return None
#
# def answer(classes, parent, child):
#     if not(parent or child) in classes or not found_path(classes, child, parent):
#         return 'No'
#     return 'Yes'
#
# n = int(input())
# for _ in range(n):
#     class_description = input().split()
#     class_name = class_description[0]
#     class_parents = class_description[2:]
#     add_class(classes, class_name, class_parents)
#
# q = int(input())
# for _ in range(q):
#     question = input().split()
#     parent = question[0]
#     child = question[1]
#     print(answer(classes, parent, child))


# n = int(input())
#
# parents = {}
# for _ in range(n):
#     a = input().split()
#     parents[a[0]] = [] if len(a) == 1 else a[2:]
#
# def is_parent(child, parent):
#     return child == parent or any(map(lambda p: is_parent(p, parent), parents[child]))
#
# q = int(input())
# for _ in range(q):
#     a, b = input().split()
#     print("Yes" if is_parent(b, a) else "No")

# class ExtendedStack(list):
#     def sum(self, *a):
#         # операция сложения
#         self.extend(a)
#         self.append(self.pop() + self.pop())
#     def sub(self):
#         # операция вычитания
#         self.append(self.pop() - self.pop())
#     def mul(self):
#         # операция умножения
#         self.append(self.pop() * self.pop())
#     def div(self):
#         # операция целочисленного деления
#         self.append(self.pop() // self.pop())
# x = ExtendedStack()
# x.sum(2, 4)
#
# def test():
#     ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
#     ex_stack.div()
#     assert ex_stack.pop() == 2
#     ex_stack.sub()
#     assert ex_stack.pop() == 6
#     ex_stack.sum()
#     assert ex_stack.pop() == 7
#     ex_stack.mul()
#     assert ex_stack.pop() == 2
#     assert len(ex_stack) == 0
#
# print(test())


# import time
#
# import time
#
# class Loggable:
#     def log(self, msg):
#         print(str(time.ctime()) + ": " + str(msg))
#
# class LoggableList(list, Loggable):
#     def append(self, msg):
#         self.log(msg)
#         list.append(self, msg)
#
# def test():
#     t = LoggableList()
#     t.append(1)
#     t.append('str')
#
#     assert len(t) == 2
#
# if __name__ == "__main__":
#     test()
