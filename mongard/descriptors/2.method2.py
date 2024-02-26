
class One:
    def __set_name__(self, owner, v):
        # همون اسمی که تو کلاس پرسن هست رو میذاره
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
    # این اسمارو میذاره
    name = One()
    car = One()

    def __init__(self, name, car) -> None:
        self.name = name
        self.car = car


x = Person("yasin", "L90")
print(x.name, x.car)
del x.car
print(x.car)
