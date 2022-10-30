d1 = {'a': 7, 'b': 3}
d2 = dict([[1, 2], [2, 3]])
d3 = dict.fromkeys('1')

price = {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2}

users = {
    'Alex7': {'password': 9876543, 'id': 1957},
    'Jimmy99': {'password': 7654837, 'id': 9654},
    'Bob31': {'password': 95463234, 'id': 6453}
}


def buy():
    pay = 0
    while True:
        enter = input('What do you buy?\n')
        if enter == 'end':
            break
        pay += price[enter]
    return pay


# d5 = d1.copy()
# print(d1.items())
# print(d1.keys())
# print(d1.values())
# d1.update(d2)
# print(d1)


if 'c' in d1:
    d1['c']

y = d1.get('c', 'value')
print(y)
