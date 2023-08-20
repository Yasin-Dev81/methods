
def def_1(*args) :# arguments
    print (args)

def def_2(**kwargs) :# keyword arguments
    print (kwargs)

def def_3(*args, **kwargs) :# tartib mohem ast.
    print (args, kwargs)

def_1(1, 2.3, "hi", [1, 2.6, "j"])
def_2(a=2, b=3.5, c="hi", d=[1, 2.6, "j"])
def_3(1, 2.3, "hi", [1, 2.6, "j"], a=2, b=3.5, c="hi", d=[1, 2.6, "j"])

"""Scope"""
x = 1 # global scope

def def_4() : 
    x = 2 # local scope
    print ("x(def_4) :", x)

def def_5() : 
    print ("x(def_5) :", x) # scope resolution

def def_6() : 
    x = 3 
    def def_7() :
        print ("x(def_7) :", x)
    def_7()
    print ("x(def_6) :", x)

def def_8() : 
    global x # change in global scope
    x += 10
    print ("x(def_8) :", x)

print ("x :", x)
def_4()
def_5()
def_6()
def_8()
print ("x :", x)

