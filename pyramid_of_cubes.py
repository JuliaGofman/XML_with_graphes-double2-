'''
Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML
документа имеет ценность 1. Кубики, расположенные прямо под ним, имеют ценность 2.
Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3. И т. д.

Ценность цвета равна сумме ценностей всех кубиков этого цвета.

Выведите через пробел три числа: ценности красного, зеленого и синего цветов.

'''

from xml.etree import ElementTree

# with open('cubes.xml', 'w') as f:
#     f.write(input())

def recurcionForCubes(el, root, value):
    value += 1
    dict_value[el.attrib['color']] += [value]
    for child in el:
        if child in el:
            recurcionForCubes(child, el, value)

# tree = ElementTree.parse('cubes.xml')
# root = tree.getroot()

#  или просто считывая через строку:
root = ElementTree.fromstring(input())

dict_value = {'red':[0], 'green':[0], 'blue':[0]}
dict_value[root.attrib['color']] += [1]

#  без рекурсии, пробегая сразу итератором. Жаль, нельзя его использовать здесь.
# for el in root.iter('cube'):
#     if el.attrib['color'] == 'red':
#         val_red += 1
#     if el.attrib['color'] == 'green':
#         val_green += 1
#     if el.attrib['color'] == 'blue':
#         val_blue += 1

for el in root:
    value = 1
    recurcionForCubes(el, root, value)
print('{} {} {}'.format(sum(dict_value['red']), sum(dict_value['green']), sum(dict_value['blue'])))

# tree.write('cubes.xml')
