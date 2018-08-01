from xml.etree import ElementTree

# with open('cubes.xml', 'w') as f:
#     f.write(input())
def recurcionForCubes(el, root, value):
    value += 1
    dict_value[el.attrib['color']] += [value]
    for child in el:
        if child in el:
            recurcionForCubes(child, el, value)

tree = ElementTree.parse('cubes.xml')
root = tree.getroot()
dict_value = {'red':[0], 'green':[0], 'blue':[0]}
# for el in root.iter('cube'):
#     if el.attrib['color'] == 'red':
#         val_red += 1
#     if el.attrib['color'] == 'green':
#         val_green += 1
#     if el.attrib['color'] == 'blue':
#         val_blue += 1

for el in root:
    value = 0
    recurcionForCubes(el, root, value)
print('{} {} {}'.format(dict_value['red'], dict_value['green'], dict_value['blue']))

# tree.write('cubes.xml')
