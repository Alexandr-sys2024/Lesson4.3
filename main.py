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

# Класс Animal для описания животных
class Animal:
    def __init__(self, species, name, age):
        self.species = species  # Вид животного (например, "Лев", "Зебра")
        self.name = name  # Имя животного
        self.age = age  # Возраст животного

    def __str__(self):
        return f"{self.species} по имени {self.name}, возраст {self.age}"

# Класс Employee для описания сотрудников
class Employee:
    def __init__(self, name, position):
        self.name = name  # Имя сотрудника
        self.position = position  # Должность (например, "Кипер", "Ветеринар")

    def __str__(self):
        return f"{self.name}, должность: {self.position}"

# Подкласс ZooKeeper (Смотритель зоопарка)
class ZooKeeper(Employee):
    def feed_animal(self, animal: Animal):
        print(f"{self.name} кормит {animal.name}, которое является {animal.species}.")

# Подкласс Veterinarian (Ветеринар)
class Veterinarian(Employee):
    def heal_animal(self, animal: Animal):
        print(f"{self.name} лечит {animal.name}, которое является {animal.species}.")

# Класс Zoo для управления животными и сотрудниками
class Zoo:
    def __init__(self, name):
        self.name = name  # Название зоопарка
        self.animals = []  # Список животных
        self.employees = []  # Список сотрудников

    # Метод для добавления животного
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлено животное: {animal}")

    # Метод для добавления сотрудника
    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Добавлен сотрудник: {employee}")

    # Метод для вывода списка всех животных
    def list_animals(self):
        print(f"\nЖивотные в зоопарке {self.name}:")
        for animal in self.animals:
            print(animal)

    # Метод для вывода списка всех сотрудников
    def list_employees(self):
        print(f"\nСотрудники в зоопарке {self.name}:")
        for employee in self.employees:
            print(employee)

# Пример использования
if __name__ == "__main__":
    # Создаем зоопарк
    zoo = Zoo("Большой зоопарк")

    # Создаем несколько животных
    lion = Animal("Лев", "Симба", 5)
    zebra = Animal("Зебра", "Марти", 7)

    # Создаем сотрудников
    keeper = Employee("Алексей", "Кипер")
    vet = Employee("Мария", "Ветеринар")

    # Добавляем животных и сотрудников в зоопарк
    zoo.add_animal(lion)
    zoo.add_animal(zebra)

    zoo.add_employee(keeper)
    zoo.add_employee(vet)

    # Выводим списки животных и сотрудников
    zoo.list_animals()
    zoo.list_employees()

