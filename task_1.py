# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass


class Tree:
    """
    Класс, описывающий дерево.

    Атрибуты:
        species (str): вид дерева (например, «дуб», «берёза»).
        height (float): высота дерева в метрах.
        age (int): возраст дерева в годах.

    Примеры:
        >>> tree = Tree("дуб", 15.5, 50)
        >>> tree.grow(5)
        >>> print(tree.height)
        20.5
    """

    def __init__(self, species: str, height: float, age: int):
        """
        Инициализирует экземпляр класса Tree.

        Аргументы:
            species (str): вид дерева.
            height (float): высота дерева (должно быть > 0).
            age (int): возраст дерева (должно быть >= 0).

        Примеры:
            >>> tree = Tree("берёза", 10.0, 30)
        """
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительной.")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным.")
        self.species = species
        self.height = height
        self.age = age

    def grow(self, growth: float) -> None:
        """
        Увеличивает высоту дерева на заданное значение.

        Аргументы:
            growth (float): величина прироста высоты (должно быть > 0).

        Примеры:
            >>> tree = Tree("сосна", 10.0, 20)
            >>> tree.grow(2.5)
            >>> print(tree.height)
            12.5
        """
        if growth <= 0:
            raise ValueError("Прирост высоты должен быть положительным.")
        self.height += growth

    def age_up(self, years: int) -> None:
        """
        Увеличивает возраст дерева на заданное количество лет.

        Аргументы:
            years (int): количество лет для увеличения возраста (должно быть > 0).

        Примеры:
            >>> tree = Tree("клён", 8.5, 15)
            >>> tree.age_up(5)
            >>> print(tree.age)
            20
        """
        if years <= 0:
            raise ValueError("Количество лет должно быть положительным.")
        self.age += years

    def get_info(self) -> str:
        """
        Возвращает строку с информацией о дереве.

        Возвращает:
            str: строка с данными о виде, высоте и возрасте дерева.

        Примеры:
            >>> tree = Tree("ясень", 12.3, 45)
            >>> print(tree.get_info())
            Вид: ясень, высота: 12.3 м, возраст: 45 лет
        """
        return f"Вид: {self.species}, высота: {self.height} м, возраст: {self.age} лет"


class Car:
    """
    Класс, описывающий автомобиль.

    Атрибуты:
        brand (str): марка автомобиля.
        model (str): модель автомобиля.
        fuel_level (float): уровень топлива в баке (в литрах).

    Примеры:
        >>> car = Car("Toyota", "Camry", 50.0)
        >>> car.drive(100)
        >>> print(car.fuel_level)
        30.0
    """

    def __init__(self, brand: str, model: str, fuel_level: float):
        """
        Инициализирует экземпляр класса Car.

        Аргументы:
            brand (str): марка автомобиля.
            model (str): модель автомобиля.
            fuel_level (float): уровень топлива (должно быть >= 0 и <= 100).

        Примеры:
            >>> car = Car("BMW", "X5", 75.0)
        """
        if fuel_level < 0 or fuel_level > 100:
            raise ValueError("Уровень топлива должен быть в диапазоне от 0 до 100 литров.")
        self.brand = brand
        self.model = model
        self.fuel_level = fuel_level

    def drive(self, distance: float) -> None:
        """
        Уменьшает уровень топлива в зависимости от пройденного расстояния.

        Аргументы:
            distance (float): пройденное расстояние в километрах (должно быть > 0).

        Примеры:
            >>> car = Car("Ford", "Focus", 60.0)
            >>> car.drive(50)
            >>> print(car.fuel_level)
            40.0
        """
        if distance <= 0:
            raise ValueError("Пройденное расстояние должно быть положительным.")
        fuel_consumption = distance * 0.4  # расход топлива: 0.4 л/км
        if fuel_consumption > self.fuel_level:
            raise ValueError("Недостаточно топлива для поездки.")
        self.fuel_level -= fuel_consumption

    def refuel(self, amount: float) -> None:
        """
        Заправляет автомобиль.

        Аргументы:
            amount (float): количество литров топлива для заправки (должно быть > 0).

        Примеры:
            >>> car = Car("Mercedes", "E-Class", 30.0)
            >>> car.refuel(20)
            >>> print(car.fuel_level)
            50.0
        """
        if amount <= 0:
            raise ValueError("Количество топлива для заправки должно быть положительным.")
        self.fuel_level = min(100, self.fuel_level + amount)  # максимум 100 литров

    def get_car_info(self) -> str:
        """
        Возвращает строку с информацией об автомобиле.

        Возвращает:
            str: строка с данными о марке, модели и уровне топлива.

        Примеры:
            >>> car = Car("Audi", "A6", 85.0)
            >>> print(car.get_car_info())
            Марка: Audi, модель: A6, топливо: 85.0 л
        """
        return f"Марка: {self.brand}, модель: {self.model}, топливо: {self.fuel_level} л"


class Book:
    """
    Класс, описывающий книгу.

    Атрибуты:
        title (str): название книги.
        author (str): автор книги.
        pages (int): количество страниц в книге.

    Примеры:
        >>> book = Book("Война и мир", "Л. Н. Толстой", 1225)
        >>> book.read(100)
        >>> print(book.pages_left)
        1125
    """

    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализирует экземпляр класса Book.

        Аргументы:
            title (str): название книги.
            author (str): автор книги.
            pages (int): количество страниц (должно быть > 0).

        Примеры:
            >>> book = Book("1984", "Джордж Оруэлл", 328)
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным.")
        self.title = title
        self.author = author
        self.pages = pages
        self._pages_read = 0  # приватный атрибут для отслеживания прочитанных страниц

    def read(self, pages: int) -> None:
        """
        Отмечает прочитанные страницы.

        Аргументы:
            pages (int): количество прочитанных страниц (должно быть > 0 и не превышать общее количество страниц).

        Примеры:
            >>> book = Book("Гарри Поттер", "Дж. К. Роулинг", 607)
            >>> book.read(50)
            >>> print(book.pages_left)
            557
        """
        if pages <= 0:
            raise ValueError("Количество прочитанных страниц должно быть положительным.")
        if pages > self.pages - self._pages_read:
            raise ValueError("Нельзя прочитать больше страниц, чем осталось в книге.")
        self._pages_read += pages

    @property
    def pages_left(self) -> int:
        """
        Возвращает количество оставшихся страниц.

        Возвращает:
            int: количество страниц, которые ещё не прочитаны.

        Примеры:
                   >>> book = Book("Преступление и наказание", "Ф. М. Достоевский", 500)
                   >>> book.read(100)
                   >>> print(book.pages_left)
                   4
        """