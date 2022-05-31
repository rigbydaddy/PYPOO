
from abc import ABC, abstractmethod
import os, math
from tokenize import Double
from Shape import Shape

class Circle(Shape):
    def __init__(self, color, filled, radius = 1.0):
        super().__init__(color, filled)
        self._radius = radius 
        

    def get_radius(self):
        return self._radius
        
    def set_radius(self, x):
        self._radius = x

    def getArea(self, radius) -> Double:
        area = math.pi * (radius ** 2)
        return area

    def getPerimeter(self, radius) -> Double:
        perimetro = 2 * math.pi * radius
        return perimetro

    def __str__(self) -> str:
        return f'Circle[{super(Circle, self).__str__()}, Radius = {self._radius}]'

print('--------------------------')
print('--------------------------')
print('--------------------------')

oval = Circle('Yellow', False)
print('PERIMETER OF CIRCLE:')
print(oval.getPerimeter(5))
print('AREA OF CIRCLE:')
print(oval.getArea(5))
print(oval)
