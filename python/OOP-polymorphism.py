"""polymorphism""" # چندريختي
# مجبور كردن ارث بر ها به پياده سازي يك متد
# exampel : area metod

class Shape :
    def __init__(self, kind, name) :
        self.kind = kind
        self.name = name
    
    def area(self) :
        raise NotImplementedError("All children of shape class should redefine the area method.")


class Square(Shape) :
    def __init__(self, kind, name, side_length):
        super().__init__(kind, name)
        self.side_length = side_length

class Circle(Shape) :
    def __init__(self, kind, name, r):
        super().__init__(kind, name)
        self.r = r

    def area(self):
        return (3.14 * self.r**2)


A = Circle("circle", "a", 10) 
print ("area of A :", A.area()) # returned area

B = Square("square", "b", 20)
print ("area of B :", B.area()) # returned error
