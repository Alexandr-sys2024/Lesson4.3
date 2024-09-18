# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассах")

    def eat(self):
        print(f"{self.name} ест.")

# Подкласс Bird, наследующий от Animal
class Bird(Animal):
    def __init__(self, name, age, can_fly=True):
        super().__init__(name, age)
        self.can_fly = can_fly

    def make_sound(self):
        print(f"{self.name} поет: Чирик-чирик!")

    def fly(self):
        if self.can_fly:
            print(f"{self.name} летает.")
        else:
            print(f"{self.name} не может летать.")

# Подкласс Mammal, наследующий от Animal
class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} говорит: Мяу-Мяу или Гав-Гав!")

# Подкласс Reptile, наследующий от Animal
class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} издает звук: Шшшш!")

# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Пример использования
if __name__ == "__main__":
    # Создаем несколько объектов животных
    bird = Bird("Попугай", 2)
    mammal = Mammal("Кошка", 4)
    reptile = Reptile("Змея", 3)

    # Список животных
    animals = [bird, mammal, reptile]

    # Вызов метода для каждого животного
    animal_sound(animals)

    # Дополнительные методы
    bird.eat()
    bird.fly()
    mammal.eat()
    reptile.eat()

