class Animal:
    """
    Базовый класс для всех животных.
    """
    def __init__(self, name: str, age: int, diet: str):
        """
        Конструктор базового класса.
        :param name: имя животного
        :param age: возраст животного (в годах)
        :param diet: тип питания (например, "травоядное", "хищник")
        """
        self.name = name
        self.age = age
        self.diet = diet

    def __str__(self) -> str:
        """Магический метод для строкового представления объекта."""
        return f"Животное: {self.name}, возраст: {self.age} лет, питание: {self.diet}"

    def __repr__(self) -> str:
        """Магический метод для официального представления объекта."""
        return f"Animal(name='{self.name}', age={self.age}, diet='{self.diet}')"

    def make_sound(self) -> str:
        """
        Метод, описывающий звук, который издаёт животное.
        В дочерних классах должен быть перегружен.
        :return: строка с описанием звука
        """
        return "Неизвестно"



class Pet(Animal):
    """
    Класс домашних животных, наследуется от Animal.
    """
    def __init__(self, name: str, age: int, diet: str, trained: bool = False):
        """
        Расширяем конструктор базового класса.
        :param trained: признак того, что животное поддаётся дрессировке
        """
        super().__init__(name, age, diet)  # вызываем конструктор родителя
        self.trained = trained  # новый атрибут для домашних животных

    def __str__(self) -> str:
        """Переопределяем строковое представление для домашних животных."""
        return f"{super().__str__()}, поддаётся дрессировке: {self.trained}"

    def __repr__(self) -> str:
        """Переопределяем официальное представление."""
        return f"Pet(name='{self.name}', age={self.age}, diet='{self.diet}', trained={self.trained})"

    def make_sound(self) -> str:
        """
        Перегружаем метод make_sound для домашних животных.
        Причина перегрузки: домашние животные издают звуки, характерные для их вида (например, «гав» у собак).
        :return: звук, характерный для домашнего животного
        """
        if self.name.lower() == "кошка":
            return "Мяу!"
        elif self.name.lower() == "собака":
            return "Гав!"
        else:
            return "Звуки домашнего животного"

    def train(self) -> None:
        """
        Метод для дрессировки животного.
        Изменяет атрибут trained на True.
        """
        self.trained = True
        print(f"{self.name} теперь поддаётся дрессировке!")


class WildAnimal(Animal):
    """
    Класс диких животных, наследуется от Animal.
    """
    def __init__(self, name: str, age: int, diet: str, habitat: str):
        """
        Расширяем конструктор базового класса.
        :param habitat: среда обитания животного (например, "лес", "саванна")
        """
        super().__init__(name, age, diet)
        self.habitat = habitat  # новый атрибут для диких животных

    def __str__(self) -> str:
        """Переопределяем строковое представление для диких животных."""
        return f"{super().__str__()}, среда обитания: {self.habitat}"

    def __repr__(self) -> str:
        """Переопределяем официальное представление."""
        return f"WildAnimal(name='{self.name}', age={self.age}, diet='{self.diet}', habitat='{self.habitat}')"

    def make_sound(self) -> str:
        """
        Перегружаем метод make_sound для диких животных.
        Причина перегрузки: дикие животные издают звуки, характерные для их среды обитания (например, рык льва).
        :return: звук, характерный для дикого животного
        """
        if self.name.lower() == "лев":
            return "Рык!"
        elif self.name.lower() == "тигр":
            return "Рёв!"
        else:
            return "Звуки дикого животного"

    def hunt(self) -> str:
        """
        Метод, описывающий охоту животного.
        :return: строка с описанием охоты
        """
        return f"{self.name} охотится в {self.habitat}!"


if __name__ == "__main__":
    # Создаём экземпляры классов
    dog = Pet("Бобик", 3, "хищник", trained=False)
    cat = Pet("Мурка", 2, "хищник")
    lion = WildAnimal("Лев", 5, "хищник", "саванна")
    elephant = WildAnimal("Слон", 10, "травоядное", "джунгли")

    # Выводим информацию о животных
    print(dog)
    print(cat)
    print(lion)
    print(elephant)

    # Используем методы
    dog.train()
    print(dog.make_sound())
    print(lion.make_sound())
    print(elephant.hunt())