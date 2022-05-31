
   
from Rectangle import Rectangle




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
sqr = Square('Black', True)
sqr.setSide(10)
print('AREA OF SQUARE')
print(sqr.getArea())
print('PERIMETER OF SQUARE')
print(sqr.getPerimeter())
print(sqr)