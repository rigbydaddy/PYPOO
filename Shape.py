from abc import ABC, abstractmethod
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
















