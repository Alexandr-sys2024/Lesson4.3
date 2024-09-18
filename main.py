class Animal:

    def __int__(self, name,age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} создает звук")

    def eat(self):
        print(f"{self.name} ест")

class Bird(Animal):
    def __int__(self, name, age, favorite_food):
        super().__int__(self, name, age)
        self.favorite_food = favorite_food

    def make_sound(self):
        print(f"{self.name} курлык")

    def eat(self):
        print(f"{self.name} ест")

class Mammal(Animal):
    def __int__(self, name, age, favorite_food):
        super().__int__(self, name, age)
        self.favorite_food = favorite_food

    def make_sound(self):
        print(f"{self.name} муууу")

    def eat(self):
        print(f"{self.name} ест")

class Reptile(Animal):
    def __int__(self, name, age, favorite_food):
        super().__int__(self, name, age)
        self.favorite_food = favorite_food

    def make_sound(self):
        print(f"{self.name} ссссс")

    def eat(self):
        print(f"{self.name} ест")