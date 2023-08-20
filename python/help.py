help(print)
print ("-"*10)
help(max)
print ("-"*10)

def def_1(num1 : float or int, num2 : float or int) -> float or int :
    """This function calculates sum of two inputs
    num1: the 1th number
    num2: the 2nd number"""
    return num1 + num2

help(def_1)
print ("-"*10)

class shapes :
    """shape of class"""
    countery = "iran" # class attribute

    def __init__(self,NAME,COLOR) :
        self.name=NAME
        self.color=COLOR

    def data(self) :
        """return data"""
        return self.name, self.color, self.countery

help(shapes)