
from abc import ABC, abstractmethod
import os, math
from tokenize import Double
from Shape import Shape  

class EquilateralTriangle(Shape):
    def __init__(self, color:str, filled:bool = True, sideLength:Double = 1.0):
        super().__init__(color, filled)
        self._sideLength = sideLength

    def getSideLength(self) -> Double:
        return self._sideLength

    def setSideLength(self, _sideLength:Double) -> Double:
        self._sideLength = _sideLength

    def getArea(self) -> Double:
        area = ((self._sideLength ** 2) * (math.sqrt(3)))/4
        return area
    def getPerimeter(self) -> Double:
        perimetro = self._sideLength * 3
        return perimetro
    
    def __str__(self) -> str:
        return f'Equilateral Triangle[{super(EquilateralTriangle, self).__str__()}, side length = {self._sideLength}]'
    
print('--------------------------')
print('--------------------------')
print('--------------------------')

eq = EquilateralTriangle('Brown')
eq.setSideLength(6)
print('AREA OF EQUILATERAL TRIANGLE')
print(eq.getArea())
print('PERIMETER OF EQUILATERAL TRIANGLE')
print(eq.getPerimeter())
print(eq)