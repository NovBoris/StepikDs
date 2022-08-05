# Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе
# Чикаго с 2001 года по настоящее время.
#
# Одним из атрибутов преступления является его тип – Primary Type.
#
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

# import csv
# import collections
# primary_type = collections.Counter()
# with open('Crimes.csv') as f:
#     # result = collections.Counter(row[5] for row in csv.reader(f) if '2015' in row[2])
#     # print(result.most_common(1))
#     reader = csv.reader(f)
#     # print(collections.Counter(row[5] for row in reader if '2015' in row[2]))
#     for row in reader:
#         if '2015' in row[2]:
#             primary_type[row[5]] += 1
# print(primary_type)

# второй вариант

# import csv
#
# with open("Crimes.csv") as fi:
#     reader = csv.reader(fi)
#     next(reader)
#     crime_cnt = dict()
#     for row in reader:
#         year = row[2][6:10]
#         if year == "2015":
#             crime_type = row[5]
#             if crime_type not in crime_cnt:
#                 crime_cnt[crime_type] = 0
#             crime_cnt[crime_type] += 1
#
# a = list(map(lambda x: (crime_cnt[x], x), crime_cnt))
# a.sort(key=lambda x: -x[0])
#
# print(a[0][1])

# Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов, которые соответствуют классам.
# У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents,
# которое содержит список имен прямых предков.
#
# Пример:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
#
# Эквивалент на Python:
#
# class A:
#     pass
#
# class B(A, C):
#     pass
#
# class C(A):
#     pass
#
# Гарантируется, что никакой класс не наследуется от себя явно или косвенно,
# и что никакой класс не наследуется явно от одного класса более одного раза.
#
# Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.
#
# <имя класса> : <количество потомков>
#
# Выводить классы следует в лексикографическом порядке.

# import json
#
# initial = json.loads(input())
#
# with_children = {element['name']: [] for element in initial}
#
# for eli in initial:
#     for elc in with_children:
#         if elc in eli['parents']:
#             with_children[elc].append(eli['name'])
#
# for element in with_children:
#     with_children[element] = set(with_children[element])
#
# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     for next in graph[start] - visited:
#         dfs(graph, next, visited)
#     return visited
#
# for element in sorted(with_children.keys()):
#     print(element, ':', len(dfs(with_children, element)))
#
# # второй вариант
#
# import json
#
# scheme = json.loads(input())
# # scheme = [{"A": []}, {"B": ["A"]}, {"C": ["A"]}, {"D": ["B", "C"]}, {"V": ["D"]}]
#
# parent_and_children = {item['name']: [] for item in scheme}
# # {'A': [], 'B': [], 'C': [], 'D': [], 'V': []}
#
# for item in scheme:
#     for parent in parent_and_children:
#         if parent in item['parents']:
#             parent_and_children[parent].append(item['name'])
# # {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': ['V'], 'V': []}
# # если класс есть в parents - его прямые дети добавляются в словарь
#
# for item in parent_and_children:
#     parent_and_children[item] = set(parent_and_children[item])
# # {'A': {'C', 'B'}, 'B': {'D'}, 'C': {'D'}, 'D': {'V'}, 'V': set()}
# # словари с детьми преобразуются в множества
#
#
# # https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     for upcoming in graph[start] - visited:
#         dfs(graph, upcoming, visited)
#     return visited
#
#
# # parent_and_children = {'A': {'C', 'B'}, 'B': {'D'}, 'C': {'D'}, 'D': {'V'}, 'V': set()}
# # dfs(parent_and_children, 'A') = {'A', 'D', 'C', 'V', 'B'}
# for item in sorted(parent_and_children.keys()):
#     print(item, ':', len(dfs(parent_and_children, item)))
#
# # третий вариант
#
# import json
#
# data = json.loads(input())
# children = dict()
#
# for cls in data:
#     for par in cls["parents"]:
#         if par not in children:
#             children[par] = []
#         children[par].append(cls["name"])
#
# def dfs(v, used):
#     size = 1
#     used.add(v)
#     if v not in children:
#         return size
#
#     for child in children[v]:
#         if child not in used:
#             size += dfs(child, used)
#
#     return size
#
# ans = []
#
# for cls in data:
#     ans.append((cls["name"], dfs(cls["name"], set())))
#
# for i in sorted(ans):
#     print(i[0], ":", i[1])
