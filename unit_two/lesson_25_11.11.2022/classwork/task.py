1. Поймите для чего служит данный паттерн
2. Ознакомьтесь со схемой паттерна в графической натации OMT
3. Установите по натации взаимодействие классов, объектов и поведения
4. Сравните натацию с кодом представленным в этом листинге
5. Проанализируйте работу кода
6. Переименуйте систему классов согласно контексту задачи

Задача:
Создайте на базе кода решение которое конструирует объект состоящий из разных частей:
Пример:
Объект компьютер состоит из устройств:
1. Процессора
2. Оперативной памяти
3. Материнской платы
4. Жесткого диска

Для каждого компьютера может быть различный тип устройств.



"""
Separate the construction of a complex object from its representation so
that the same construction process can create different representations.
"""

import abc


class Director:
    """
    Construct an object using the Builder interface.
    """

    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self._builder = builder
        self._builder._build_part_a()
        self._builder._build_part_b()
        self._builder._build_part_c()


class Builder(metaclass=abc.ABCMeta):
    """
    Specify an abstract interface for creating parts of a Product
    object.
    """

    def __init__(self):
        self.product = Product()

    @abc.abstractmethod
    def _build_part_a(self):
        pass

    @abc.abstractmethod
    def _build_part_b(self):
        pass

    @abc.abstractmethod
    def _build_part_c(self):
        pass


class ConcreteBuilder(Builder):
    """
    Construct and assemble parts of the product by implementing the
    Builder interface.
    Define and keep track of the representation it creates.
    Provide an interface for retrieving the product.
    """

    def _build_part_a(self):
        pass

    def _build_part_b(self):
        pass

    def _build_part_c(self):
        pass


class Product:
    """
    Represent the complex object under construction.
    """

    pass


def main():
    concrete_builder = ConcreteBuilder()
    director = Director()
    director.construct(concrete_builder)
    product = concrete_builder.product


if __name__ == "__main__":
    main()