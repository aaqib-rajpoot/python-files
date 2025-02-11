class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def speek(self):
        print(f"{self.name} is speaking")

class Dog(Animal):
    pass

StreetDog = Dog("Tom","something")
StreetDog.speek()
