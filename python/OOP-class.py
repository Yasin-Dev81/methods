
class shapes :
    countery = "iran" # Class attribute

    def __init__(self,NAME,COLOR) : # Instance attribute
        self.name=NAME
        self.color=COLOR

A=shapes('cube','red')
B=shapes('circle','green')
C=shapes('pentagon','blue')

A.owner = 'yasin' # adding a self 

print (A.color)
del A.color  #delete color

print(B.name)
print(B.__dict__)
print(B.__dict__.keys())

C.countery = "USA" # change class attribute
print (C.countery)

del C.countery # delete (class/instance) attribute
print (C.countery)

C.name = "circle" # change instance attribute
print (C.name)


"""Inheritance""" # وراثت

class Car(shapes) :

    def data(self) :
        return (self.name, self.color, self.countery)

D = Car('circle','blue')
print (D.data())

class Truck(shapes) :

    def __init__(self, NAME, COLOR, types):
        super().__init__(NAME, COLOR)
        self.types = types

    def data(self) :
        return (self.name, self.color, self.countery, self.types)

E = Truck('circle','blue', "TT")
print (E.data())

class FireTruck(shapes) :

    def __init__(self, COLOR, types):
        super().__init__("fire truck", COLOR)
        self.types = types

    def data(self) :
        return (self.name, self.color, self.countery, self.types)

F = FireTruck('blue', "FT")
print (F.data())

"""Method Resolution order""" # مسير ارث بري
# exampel :
# Method resolution order in Truck() :
# 1) Truck
# 2) shapes
# 3) builtins.object
help(Truck)
