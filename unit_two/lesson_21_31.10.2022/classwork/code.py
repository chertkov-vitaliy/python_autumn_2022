import psycopg2
try:
    conn = psycopg2.connect(
            dbname = "python_test",
            user = "WRONG_USER",
            host = "localhost",
            password = "mypass"
        )
except Exception as e:
    print(e)
    # print(dir(e))
    # print(e.pgcode)
    # print(e.pgerror)
    # print(e.diag)



#
# class NegValException(Exception):
#     def __init__(self, number):
#         super().__init__(f"Neg val:  {number}")
#         self.number = number


#1. Реализовать свой класс exception


#
# login = "admim"
# class LoginNotFound(Exception):
#     def __init__(self):
#         super().__init__("Логин не найден")
#         "Логин не с"
#
# try:
#     if login != "admin":
#         raise LoginNotFound()
# except LoginNotFound as e:
#     print(e)
# else:
#     print("Eception не случился!")
# finally:
#     print("Блок сработает в любом случае")
#
#
# try:
#     fd = open('file.txt', mode="r")
# except FileNotFoundError:
#     print("FileNotFoundError")
#     fd = None
# except Exception:
#     fd = None
#     print("Exception")
#
# if not fd:
#     print("Файл не найден!")