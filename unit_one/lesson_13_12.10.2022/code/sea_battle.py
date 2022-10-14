from random import randint as rdi
game_field = []
LIVE = 1
import sys

def init():
    result = matrix()
    print(result)

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
            game_field[i][j]  = -1
            print("Попал")
        else:
            minus_live()
    else:
        print("Ваша песенка спета!")

menu()





