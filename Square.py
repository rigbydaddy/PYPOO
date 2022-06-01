
   
from tokenize import Double
from Rectangle import Rectangle




class Square(Rectangle):
    def __init__(self, color:str, filled:bool, side:Double):
        super().__init__(color, filled, width=side, length=side)

    def getSide(self) -> Double:
        return self._width

    def setSide(self, side:Double) -> Double:
        self.setWidth(side)
        self.setLength(side)

    def setWidth(self, side:Double) -> Double:
        self._width = self._length = side

    def setLength(self, side:Double) -> Double:
        self._width = self._length = side
    
    def __str__(self) -> str:
        return f'Square[{super(Square, self).__str__()}]'

print('--------------------------')
print('--------------------------')
print('--------------------------')
sqr = Square('Black', True, 5)
#sqr.setSide(10)
print('AREA OF SQUARE')
print(sqr.getArea())
print('PERIMETER OF SQUARE')
print(sqr.getPerimeter())
print(sqr)