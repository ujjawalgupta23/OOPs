from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def apply_brakes(self):
        pass


class Car(Vehicle):
    def start(self):
        print("The Car has started")

    def apply_brakes(self):
        print("Car brakes have been applied")


class Bike(Vehicle):
    def start(self):
        print("The Bike has started")

    def apply_brakes(self):
        print("Bike breaks have been applied")


# Abstract Class cannot be instantiated
# v1 = Vehicle()
# v1.start()
# v1.apply_brakes()

c1 = Car()
c1.start()
c1.apply_brakes()

b1 = Bike()
b1.start()
b1.apply_brakes()