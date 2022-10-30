import math

PI = math.pi


def radius():
    n = float(input('Введите диаметр цилиндра: '))
    n /= 2
    return n


def height():
    m = float(input('Введите высоту цилиндра: '))
    return m


def volume():
    r = radius()
    h = height()
    s = PI * r ** 2
    v = s + h
    return v


def mass(g):
    n = float(input('Введите удельный вес: '))
    return g * n / 1000


print('Вес цилиндра в кг: ', mass(volume()))

# print('Объем цилиндра: ', volume(), 'см3')
