# Для запуска приложения просто запустите скрипт
# перейдите по адресу  в браузер который сгенерирует flask

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/login', methods=['GET', 'POST'])
def login():
 if request.method == 'POST':
   return "Получили данные"
 else:
   return "Форма логина"


@app.route('/student/list')
def get_list():
   # connect to DB
   return  { "id": 12, "name": "Peter I"}


if __name__ == "__main__":
    app.run()