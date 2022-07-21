# Вам дано описание пирамиды из кубиков в формате XML.
# Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue).
# Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.
#
# Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность
# 1. Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками,
# имеют ценность 3. И т. д.
#
# Ценность цвета равна сумме ценностей всех кубиков этого цвета.
#
# Выведите через пробел три числа: ценности красного, зеленого и синего цветов.

# from xml.etree import ElementTree
#
# color_count = {'blue': 0, 'red': 0, 'green': 0}
# root = ElementTree.fromstring(input())
# color_count[root.attrib['color']] += 1
#
#
# def recurs(root, level=2):
#     for row in root:
#         if row.attrib['color'] in color_count:
#             color_count[row.attrib['color']] += level
#             recurs(row, level + 1)
#
#
# recurs(root)
# print(color_count['red'], color_count['green'], color_count['blue'])
#
# # Второй вариант
#
# import xml.etree.ElementTree as ET
#
# tree = ET.fromstring(input())
# ans = {"red": 0, "green": 0, "blue": 0}
#
# def dfs(cube, res, depth):
#     res[cube.attrib["color"]] += depth
#     for i in cube.findall("cube"):
#         dfs(i, res, depth + 1)
#
# dfs(tree, ans, 1)
# print(ans["red"], ans["green"], ans["blue"])
