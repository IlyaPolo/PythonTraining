# import os
#
# list_paths = []
#
# for adress, papka, file in os.walk('D:\SteamLibrary'):
#     for i in file:
#         full_path = os.path.join(adress, i)
#         list_paths.append(full_path)

# 'r' - открыть для чтения (по умолчанию)
# 't' - открыть в текстовом режиме (по умолчанию)
# 'w' - открыть для записи, содержимое файла удалится, если файла нет, создается новый
# 'a' - открыть для дозаписи в конец файла, если файла нет, создается новый
# 'b' - открыть в бинарном режиме
# '+' - открыть для чтения и записи 'r+', 'w+', 'a+'

r = open('D:\\SteamLibrary\steamapps\common\Phasmophobia\Phasmophobia.exe', 'rb')
y = open('Копия', 'wb')

while True:
    var = r.read(1048576)
    print(var.__sizeof__())
    if var.__sizeof__() == 17:
        break

    y.write(var)

print('control')

r.close()
y.close()
