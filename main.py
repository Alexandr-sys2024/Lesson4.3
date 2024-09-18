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

import pickle

# Класс Animal для представления животных
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.species}, возраст: {self.age}"

# Базовый класс Employee для всех сотрудников зоопарка
class Employee:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Сотрудник: {self.name}"

# Подкласс ZooKeeper (Смотритель зоопарка)
class ZooKeeper(Employee):
    def feed_animal(self, animal: Animal):
        print(f"{self.name} кормит {animal.name}, которое является {animal.species}.")

# Подкласс Veterinarian (Ветеринар)
class Veterinarian(Employee):
    def heal_animal(self, animal: Animal):
        print(f"{self.name} лечит {animal.name}, которое является {animal.species}.")

# Класс Zoo для управления животными и сотрудниками (композиция)
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []   # Список для хранения животных
        self.employees = [] # Список для хранения сотрудников

    # Метод для добавления животных
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк.")

    # Метод для добавления сотрудников
    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Сотрудник {employee.name} добавлен в зоопарк.")

    # Метод для отображения всех животных
    def show_animals(self):
        print("\nЖивотные в зоопарке:")
        for animal in self.animals:
            print(animal)

    # Метод для отображения всех сотрудников
    def show_employees(self):
        print("\nСотрудники зоопарка:")
        for employee in self.employees:
            print(employee)

    # Метод для сохранения состояния зоопарка в файл
    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print(f"Информация о зоопарке '{self.name}' сохранена в файл '{filename}'.")

    # Статический метод для загрузки состояния зоопарка из файла
    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, 'rb') as file:
                zoo = pickle.load(file)
                print(f"Информация о зоопарке загружена из файла '{filename}'.")
                return zoo
        except FileNotFoundError:
            print(f"Файл '{filename}' не найден. Создается новый зоопарк.")
            return None

# Пример использования
if __name__ == "__main__":
    # Попробуем загрузить зоопарк из файла, если он существует
    filename = "zoo_data.pkl"
    zoo = Zoo.load_from_file(filename)

    # Если зоопарк не был найден в файле, создаем новый
    if zoo is None:
        zoo = Zoo("Зоопарк города")

    # Добавляем животных и сотрудников только если их еще нет
    if not zoo.animals:
        animal1 = Animal("Лев", "Хищник", 5)
        animal2 = Animal("Зебра", "Травоядное", 3)
        zoo.add_animal(animal1)
        zoo.add_animal(animal2)

    if not zoo.employees:
        zookeeper = ZooKeeper("Андрей")
        veterinarian = Veterinarian("Мария")
        zoo.add_employee(zookeeper)
        zoo.add_employee(veterinarian)

    # Выводим текущие данные зоопарка
    zoo.show_animals()
    zoo.show_employees()

    # Пример использования специфических методов сотрудников
    zookeeper.feed_animal(animal1)    # Смотритель кормит животное
    veterinarian.heal_animal(animal2) # Ветеринар лечит животное

    # Сохраняем текущее состояние зоопарка в файл
    zoo.save_to_file(filename)