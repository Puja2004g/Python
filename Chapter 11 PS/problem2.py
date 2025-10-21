class Animals:
    def __init__(self):
        print("Animals")


class Pets(Animals):
    def __init__(self):
        super().__init__()
        

class Dog(Pets):
    def __init__(self):
        pass

    def bark(self):
        super().__init__()
        print("Barking")

d = Dog()

d.bark()