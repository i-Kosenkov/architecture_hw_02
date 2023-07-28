from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Crocodile(Animal):
    def eat(self):
        return "Ням-Ням!"


class Tiger(Animal):
    def run(self):
        return "Run tiger run!"


class Fabric:
    def create_animal(self, animal_type):
        if animal_type == "Crocodile":
            return Crocodile()
        elif animal_type == "Tiger":
            return Tiger()
        else:
            return None


fabrik = Fabric()
animal = fabrik.create_animal("Crocodile")
print(animal.eat())
animal = fabrik.create_animal("Tiger")
print(animal.run())


# ------------------------------------------
class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("Singleton class!")
        else:
            Singleton.__instance = self


# ------------------------------------------
class Model:
    def __init__(self):
        self.data = []

    def add_data(self, new_data):
        self.data.append(new_data)


class ViewData:
    def show_data(self, data):
        print("Data: {}".format(data))


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = ViewData()

    def add_data(self, new_data):
        self.model.add_data(new_data)
        self.view.show_data(self.model.data)