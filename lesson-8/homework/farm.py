class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name = {self.name}, age {self.age}'

class Dog(Animal):
    def __init__(self, name, age, is_alive = True):
        super().__init__(name, age)
        self.is_alive = is_alive
    def __str__(self):
        return f'name = {self.name}, age = {self.age}, is {"alive" if self.is_alive else "dead"}'
    @staticmethod
    def speak():
        print("wow")

class Cat(Animal):
    def __init__(self, name, age, is_alive = True):
        super().__init__(name, age)
        self.is_alive = is_alive
    def __str__(self):
        return f'name = {self.name}, age = {self.age}, is {"alive" if self.is_alive else "dead"}'
    @staticmethod
    def speak():
        print("meow")

class Cow(Animal):
    def __init__(self, name, age, is_alive = True):
        super().__init__(name, age)
        self.is_alive = is_alive
    def __str__(self):
        return f'name = {self.name}, age = {self.age}, is {"alive" if self.is_alive else "dead"}'
    @staticmethod
    def speak():
        print("moo")

dog = Dog("my dog", 20, True)
cat = Cat("my cat", 10, True)
cow = Cow("my cow", 5, False)
dog.speak()
cat.speak()
cow.speak()