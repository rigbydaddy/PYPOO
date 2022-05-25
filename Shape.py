from abc import ABC, abstractmethod
import math
from tokenize import Double

class Shape(ABC):
    def __init__(self, color, filled = True):
        self._color = color
        self._filled = filled

    def get_color(self):
        return self._color
      
    def set_color(self, x):
        self._color = x

    def isFilled(self):
        return self._filled

    def setFilled(self, x):
        self._filled = x
    
    @abstractmethod
    def getArea() -> Double:
        pass

    @abstractmethod
    def getPerimeter() -> Double:
        pass

    def __str__(self) -> str:
        return f'Shape[Color = {self._color}, Filled = {self._filled}]'


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



class Rectangle(Shape):
    def __init__(self, color, filled, width = 1.0, length = 1.0):
        super().__init__(color, filled)
        self._width = width
        self._length = length


    def get_width(self):
        return self._width

        
    def set_width(self, x):
        self._width = x

    def get_length(self):
        return self._width

        
    def set_length(self, x):
        self._length = x

    def getArea(self) -> float:
        area = self._length * self._width
        return area

    def getPerimeter(self) -> float:
        perimetro = (self._length + self._width) * 2
        return perimetro

    def __str__(self) -> str:
        return f'Rectangle[{super(Rectangle, self).__str__()}, Width = {self._width}, Length = {self._length}]'

class EquilateralTriangle(Shape):
    def __init__(self, color, filled=True, sideLength = 1.0):
        super().__init__(color, filled)
        self._sideLength = sideLength

    def getSideLength(self) -> Double:
        return self._sideLength

    def setSideLength(self, _sideLength:Double) -> Double:
        self._sideLength = _sideLength

    def getArea(self) -> Double:
        area = (self._sideLength * self._sideLength)/2
        return area
    def getPerimeter(self) -> Double:
        perimetro = self._sideLength * 3
        return perimetro
    
    def __str__(self) -> str:
        return f'Equilateral Triangle[] {super(EquilateralTriangle, self).__str__()}, Side Length = {self._sideLength}]'
    

    


class Square(Rectangle):
    def __init__(self, color, filled, width=1, length=1):
        super().__init__(color, filled, width, length)

    def getSide(self) -> float:
        return self._width

    def setSide(self, side:float) -> float:
        self._width = self._length = side

    def setWidth(self, side:float) -> float:
        self._width = self._length = side

    def setLength(self, side:float) -> float:
        self._width = self._length = side
    
    def __str__(self) -> str:
        return f'Square[{super(Square, self).__str__()}]'



print('--------------------------')
print('--------------------------')
print('--------------------------')
oval = Circle('Yellow', False)
print('PERIMETER OF CIRCLE:')
print(oval.getPerimeter(5))
print('AREA OF CIRCLE:')
print(oval.getArea(5))
print(oval)
print('--------------------------')
print('--------------------------')
print('--------------------------')
rect = Rectangle('Pink', True, 5,4)
print('AREA OF RECTANGLE')
print(rect.getArea())
print('PERIMETER OF RECTANGLE')
print(rect.getPerimeter())
print(rect)
print('--------------------------')
print('--------------------------')
print('--------------------------')
sqr = Square('Black', True)
sqr.setSide(10)
print('AREA OF SQUARE')
print(sqr.getArea())
print('PERIMETER OF SQUARE')
print(sqr.getPerimeter())
print(sqr)
print('--------------------------')
print('--------------------------')
print('--------------------------')
eq = EquilateralTriangle('Brown')
eq.setSideLength(20)
print('AREA OF EQUILATERAL TRIANGLE')
print(eq.getArea())
print('PERIMETER OF EQUILATERAL TRIANGLE')
print(eq.getPerimeter())
print(eq)