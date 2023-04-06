from Circle import *
from math import pi
# import Circle

class Cylinder(Circle):
    def __init__(self, radius=1.0, height=1.0) -> None:
        super().__init__(radius)
        self.__radius = radius
        self.__height = height
        
    def get_height(self):
        return self.__height
    
    def get_volume(self):
        return self.__height * super().get_area()
    
    def get_area(self):
        return 2 * pi * self.__radius * self.__height + 2 * super().get_area()
