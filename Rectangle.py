from Shape import Shape


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


print('--------------------------')
print('--------------------------')
print('--------------------------')
rect = Rectangle('Pink', True, 5,4)
print('AREA OF RECTANGLE')
print(rect.getArea())
print('PERIMETER OF RECTANGLE')
print(rect.getPerimeter())
print(rect)