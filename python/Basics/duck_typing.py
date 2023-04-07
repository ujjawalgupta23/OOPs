""""If it walks like a duck, quacks like a duck. It must be a duck"""
class Duck:
    def walk(self):
        print("This Duck is walking")

    def talk(self):
        print("This Duck is quacking")

class Chicken:
    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person:
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the animal")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)