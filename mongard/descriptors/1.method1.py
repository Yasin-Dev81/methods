"""
- __dict__
    * همه اتربیوت ها رو تو یه دیکشنری برمیگردونه

"""

class One:
    def __init__(self, v) -> None:
        self.v = v

    def __get__(self, instance, owner):
        return instance.__dict__[self.v]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("value must be str!")
        instance.__dict__[self.v] = value

    def __delete__(self, instance):
        if self.v=="car":
            instance.__dict__[self.v] = "BiCar"
        else:
            del instance.__dict__[self.v]


class Person:
    name = One("name")
    car = One("car")

    def __init__(self, name, car) -> None:
        self.name = name
        self.car = car


x = Person("yasin", "L90")
print(x.name, x.car)
del x.car
print(x.car)
