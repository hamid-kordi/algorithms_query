class One:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("zer moft")
        instance.__dict__[self.name] = value


class person:
    name = One("name")
    car = One("car")

    def __init__(self, name, car):
        self.name = name
        self.car = car


p = person("amir", "peride")
p.name = "123456"

print(p)
