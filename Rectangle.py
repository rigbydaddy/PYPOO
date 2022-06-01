from tokenize import Double
from Shape import Shape


class Rectangle(Shape):
    def __init__(self, color:str, filled:bool, width:Double = 1.0, length:Double = 1.0):
        super().__init__(color, filled)
        self._width = width
        self._length = length


    def getWidth(self):
        return self._width

        
    def setWidth(self, width:Double):
        self._width = width

    def getLength(self):
        return self._width

        
    def setLength(self, length:Double):
        self._length = length

    def getArea(self) -> Double:
        area = self._length * self._width
        return area

    def getPerimeter(self) -> Double:
        perimetro = (self._length + self._width) * 2
        return perimetro

    def __str__(self) -> str:
        return f'Rectangle[{super(Rectangle, self).__str__()}, width = {self._width}, length = {self._length}]'


print('--------------------------')
print('--------------------------')
print('--------------------------')
rect = Rectangle('Pink', True, 5,4)
print('AREA OF RECTANGLE')
print(rect.getArea())
print('PERIMETER OF RECTANGLE')
print(rect.getPerimeter())
print(rect)