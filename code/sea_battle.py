from random import randint as rdi
import sys

access = [1, 10, 100, 200, 300]
game_field = []
LIVE = 2

def init():
    """Инициируем начальное состояние игры!
    Заполняем поле нулями.
    """
    matrix()

def decorator_access(func_menu):
    """
    Декоратор для проверки доступа пользователя к игре
    :param func_menu:
    :return wrapper:
    """
    id = int(input("Введите ID"))
    def wrapper():
        global access
        if id not in access:
            sys.exit("Нет доступа! ")
        else:
            func_menu()
    return wrapper

@decorator_access
def menu():
    out = f"1. Новая игра\n2. Продолжить игру\n3. Сохранить игру\n4.Загрузить игру"
    print(out)
    num = int(input("Раздел:"))
    if num == 1:
        init()
        game()
    else:
        sys.exit(0)

def matrix(n = 5, m = 5):
    global game_field
    game_field = [[rdi(0, 1) for _ in range(n)] for _ in range(m)]

def get_position():
    long = input("Введите координату x:")
    lot = input("Введите координату y:")
    return (int(long),int(lot))

def minus_live():
    global LIVE
    LIVE -= 1

def game():
    global game_field
    while LIVE:
        i, j = get_position()
        if game_field[i][j] == 1:
            game_field[i][j] = -1
            print("Попал")
            render()
        else:
            minus_live()
    else:
        print("Ваша песенка спета!")

def render():
    global game_field
    str = ""
    for row in game_field:
        str = "\n"
        for elm in row:
            str += f" {elm} "
        else:
            print(str)


if __name__ == "__main__":
    menu()