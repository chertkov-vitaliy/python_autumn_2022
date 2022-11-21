Структура приложения:

auth
  |--- static
         |--- css
  |--- templates
              |--- index.html
              |--- account.html
              |--- user
  |--- venv
  |--- models.py
  |--- app.py
  |--- routes.py
  |--- requirements.txt


Действия:
1. Создаем новый проект
2. В виртуальное окружение устанавливаем необходимые библиотеки Flask
Flask-SQLAlchemy
3. Добавляем установленные библиотеки в файл requirements.txt
4. Создаем файл app.py
5. Переносим в app.py приложение Flask и DB
6. Создаем в app роутер для обработки формы из документации
https://flask-sqlalchemy.palletsprojects.com/en/latest/quickstart/

@app.route("/users/create", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            email=request.form["email"],
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("user_detail", id=user.id))

    return render_template("user/create.html")

7. Переименовываем роутер в Аccount , используем класс Account вместо User
8. Создаем шаблон account.html  в папке templates
9. В шаблон html5  вставляем тег формы <form>. Внутрь тега формы вставляемя два элемента
input и кнопку submit . Задаем атрибуты тегу name - такие какие есть у нашей модели Account
10. Тестируем передачу логина и пароля на сервер Flask и запись их в БД, не забудьте использовать
для выполнения запросов к БД with app.app_context():



Индексная страница
1. Создаем роутер для индексной страницы
2. В роутере прописываем рендер index.html
3. В папку templates добавляем файл index.html
4. В index.html  помещаем текст шаблона со слайда 16 лекции 28
<html lang="ru" >
 <head>
   <meta charset="utf-8">
   <title>Flask Parent Template</title>
   <link rel="stylesheet" href="{{ url_for('static', filename='css/default.css') }}">
 </head>
 <body>
    <header>
        <h1 class="logo">First Web App</h1>
        <nav>
          <ul class="menu">
            <li><a href="{{ url_for('home') }}">Home</a></li>
            <li><a href="{{ url_for('about') }}">About</a></li>
          </ul>
        </nav>
    </header>
    {% block content %}
    {% endblock %}
 </body>
</html>

5. Корректируем ссылки на наши роутеры.
6. Создаем файл стилей(default.css) в папке static
7. Добавляем в default.css стили с сайта
https://html5css.ru/css/css_navbar.php
ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    width: 200px;
    background-color: #f1f1f1;
}

li a {
    display: block;
    color: #000;
    padding: 8px 16px;
    text-decoration: none;
}

/* Change the link color on hover */
li a:hover {
    background-color: #555;
    color: white;
}


8. Наслаждаемся красотой тестируем переходы.







