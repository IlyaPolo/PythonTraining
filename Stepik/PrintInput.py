# # Вывод последней и первой цифры двузначного числа
# num = 17
# a = num % 10
# b = num // 10
#
# # print(a)
# # print(b)
#
# # Вывод цифр трехзначного числа
#
# num = 754
# a = num % 10
# b = (num % 100) // 10
# c = num // 100
# print(a)
# print(b)
# print(c)

# num = int(input())
# a = num % 10
# b = (num % 100) // 10
# c = num // 100
#
# summ = a + b + c
# mul = a * b * c
#
# print('Сумма цифр =', summ)
# print('Произведение цифр =', mul)

# num = int(input())
# a = num % 10  # c
# b = (num % 100) // 10  # b
# c = num // 100  # a
#
# print(str(c) + str(b) + str(a))  # abc
# print(str(c) + str(a) + str(b))  # acb
# print(str(b) + str(c) + str(a))  # bac
# print(str(b) + str(a) + str(c))  # bca
# print(str(a) + str(c) + str(b))  # cab
# print(str(a) + str(b) + str(c))  # cba

# num = int(input())
# a = num % 10
# b = (num % 100) // 10
# c = (num % 1000) // 100
# d = num // 1000
#
# print('Цифра в позиции тысяч равна', d)
# print('Цифра в позиции сотен равна', c)
# print('Цифра в позиции десятков равна', b)
# print('Цифра в позиции единиц равна', a)
a = 17 // (23 % 7)
b = 34 % a * 5 - 29 % 4 * 3
print(a * b)