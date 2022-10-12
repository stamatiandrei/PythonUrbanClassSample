class Wood:
    """
    Класс описывает дерево
    """
    def __init__(self, grade: str, age: float, health=True: bool):  # FIXME health: bool = True аннотация типов для значений по умолчанию записывается таким образом
        """
        Создание и подготовка к работе объекта "Дерево"

        :param grade: Сорт дерева
        :param age: Возраст дерева
        :param helth: Здоровье дерева
        """

        self.grade = grade
        self.age = age
        self.health = health

    def get_grade(self) -> str:
        """
        Функция возвращает сорт дерева

        :return: Сорт дерева
        """
        ...

    def get_age(self) -> int:
        """
        Функция вохвращет возраст дерева

        :return: Возраст дерева
        """
        ...

    def aging(self, number_years: int) -> int:
        """
        Функция состаривает дерево

        :param number_years: Количество лет состаривания
        :return: Текущий возраст дерева
        """
        ...

    def treatment(self) -> str:
        """
        Функция лечит дерево, если оно больное

        :return: Текущее здоровье дерева
        """
        ...

class Backpack:
    """
    Класс описывает рюкзак
    """
    def __init__(self, type_backpack: str, style: str, volume: int, filling={}: dict):  # FIXME filling={} использовать изменяемые типы данных в качестве значений по умолнию не очень хорошо https://colab.research.google.com/drive/1H0SjwycQ5Dx1ArL4QHzxLgVoyzBFzCjE#scrollTo=H63BjOzcXKI0
        """
        Создание и подготовка к работе объекта "Рюкзак"

        :param type_backpack: Тип рюкзака
        :param style: Стиль рюкзака
        :param volume: Объем рюкзака
        :param filling: Наполнение рюкзака, c объемом вещи
        """

        self.type_backpack = type_backpack
        self.style = style
        self.volume = volume
        self.filling = filling

    def get_type_style(self) -> str:
        """
        Функция вывод тип и стиль рюкзака

        :return: Описание типа и стиля рюкзака
        """
        ...

    def get_free_volume(self) -> int:
        """
        Функция считает и выводит свобдный объем в рбкзаке

        :return: Свободный объем в рбкзаке
        """
        ...

    def get_filling(self) -> str:
        """
        Функция выводит наполнение и свободный объем в рюкзаке

        :return: Выводит текущее наполнение и свободный объем в рюкзаке
        """
        ...
    
    def add_thing(self, volume_thing: int, name_thing: str) -> str:
        """
        Функция проверяет хватит ли места в рюкзаке и добавлет вещь в рбкзак
        Обновляет его наполнение, добавляет в словарь name_thing:volume_thing

        :param volume_thing: Объем занимаемый вещью
        :param name_thing: Имя вещи
        :return: Оповещение добавлена ли вещь и текущий свободный объем рюкзака и список вещей 
        """
        ...

class Grandfather:
    """
    Класс описывает дедушку
    """

    def __init__(age: int, gemes: list, joke: list, level_of_intoxication: float):
        """
        Создание и подготовка к работе объекта "Дедушка"

        :param age: Возраст дедушки
        :param gemes: Список игр
        :param joke: Список анекдотов
        :param level_of_intoxication: Уровень алкогольного опьянения
        """

    def get_joke(self) -> str:
        """
        Функция выбирает случайным образом из списка анекдот и выводит его

        :return: Один из анекдотов
        """
        ...

    def play_gemes(self) -> str:
        """
        Функция случайным образом выбирает игру

        :return: Функция выводит игру
        """

    def drink_alcohol(self) -> int:
        """
        Дедушка выпивает 50 грамм и функция увеличивает значение опьянения

        :return: Выводит текущий уровень опьянения
        """
        ...

    def go_sleep(self) -> str:
        """
        Функция проверят уровень алкогольного опьянения и отправляет деда спать

        :return: Строка о том что дедушка ушел спать
        """
        ...



if __main__ = "__main__":
  print('Создайте классы Wood, Backpack, Grandfather')
