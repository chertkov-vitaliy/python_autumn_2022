#todo: Задан файл dictionary.xml (в текущей папке).
#
# <dict>
#     <key>###</key>
#     <value>##</value>
# </dict>
#
# Написать функцию которая принимает кортеж вида   и записывает его значения в файл
# Первое значение кортежа в позицию <key> второе в <value>
# Итоговый файл должен получиться:
# <dict>
# <key>'age'</key>
# <value>16</value>
# </dict>
#
# Задачу решить с помощь метода seek()


key, values = ('age', 16)

fd = open("./dictionary.xml", "r+")
fd.readline()
fd.seek(6)
fd.write(key)
