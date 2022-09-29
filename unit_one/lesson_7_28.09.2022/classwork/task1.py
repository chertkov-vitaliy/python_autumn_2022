#todo: Написать функцию logger() которая принимает в качестве аргумента текст который дописывается
# в файл error.log Новое сообщение должно распологаться на новой строчки.

FILE = "error.log"
def logger(text_):
    fd = open(FILE, mode="at")
    fd.write(text_ + "\n")
    fd.close()


logger("Error on line 26 ")

