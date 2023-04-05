from math import pi
class Circle:
    def __init__(self, radius=1.0, color='red') -> None:
        self.__radius = radius
        self.__color = color
        
    def get_radius(self):
        return self.__radius
    
    def get_area(self):
        return self.__radius ** 2 * pi
    
    def __str__(self) -> str:
        return f'radius of Circle is {self.__radius}, color is {self.__color}'
    
    
# c1 = Circle(2, "Blue")
# print(c1)