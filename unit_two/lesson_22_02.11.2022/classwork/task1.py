# todo: Реализовать функционал систем для авторизации. Любой класс можно расширить до той функциональности которая
# потребуется в результате написания кода.
class SUPER_DB(ABC):
    @abstractmethod
    def get_connect(self):
        pass

class DB_Postgres(ABC):
class DB_Mongo(ABC):
    '''Данный класс содержит конструктор и метод get_connect. В конструкторе инициализируются переменные
     (атрибуты доступа к БД) . Метод возвращает соединение.'''
    def __init__(self, dbname, user, password):
    # В констукторе инициализируем атрибуты доступа к БД
        pass

    @abstractmethod
    def get_connect(self):
        # Метод возвращает соединение к БД
        pass


class Auth:
    """Класс содержит методы регистрации, захода в систему и выхода из нее"""
    is_auth = False
    def registration(self):
        """Метод создания профиля пользователя в системе """
        pass

    def login(self):
        """Метод аутентификации пользователя в системе"""
        pass

    def logout(self):
        Auth.is_auth = False


class Profile:
    ''' Данный класс содержит конструктор и метод set_profile и get_profile для добавления и получения
     пользователя соответсвенно'''
    def __init__(self, login, password, name, surname, age, tel, email):
        """В констукторе инициализируем атрибуты сущности Profile"""
        pass

    def set_profile(self, conn):
        """в аргументе conn передается дискриптор подключения к БД"""
        # Добавляет профиль в БД
        pass

    def get_profile(self, conn):
        # Извлекает профиль из БД
        pass
