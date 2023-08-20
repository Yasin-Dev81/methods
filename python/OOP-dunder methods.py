"""Dunder methods / Magic methods""" # متد هاي جادويي

from unicodedata import decimal


class Square :
    def __init__(self, side_length:float) -> None:
        self.side_length = side_length
    
    def __str__(self) -> str:
        return "side length is %s" % self.side_length

    def __len__(self) -> float : # ميتونيم خودمون تعيينش كنيم
        return self.side_length
    
    def __del__(self) :
        print ("square with %s side length is deleted." % self.side_length)

    def __add__(self, other) :
        return self.side_length + other.side_length

square1 = Square(10)
square2 = Square(41)
print ("__str__ of square :", square1)
print ("__len__ of square (len(square)) :", len(square1))
print ("__add__ of square (Square(5)+Square(11)) :", square1+square2)

del square1 
# print (square) # returned error

print ("all methods of Square (dir(Square)):", dir(Square))

