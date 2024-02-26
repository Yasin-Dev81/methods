"""
- descriptors
    * یک روش بهتر برای مدیریت کردن اتربیوت هامونن

- property (getter), setter, deleter
    * اگه بخوایم متغیرهای داخل کلاس رو محدود و مدیریت کنیم
    * مشکل اینه که برای هر اتربیوت (متغیر) این کدارو بنویسیم و کد تکراری میشه
    * solve with (descriptors)

"""

class Person:
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    # @getattr
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Value must be str!")
        self._name = value

    @name.deleter
    def name(self):
        self._name = None



x = Person("2")
print(x.name)

del x.name
print(x.name)
