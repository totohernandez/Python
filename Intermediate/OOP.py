class Person:

    amount = 0

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1
    
    def __del__(self):
        Person.amount -= 1

    def __str__(self):
        return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)
    
    def get_older(self, years):
        self.age += years

x = Person('Mike', 30, 180)
# print(x.name)
# print(x.age)
# print(x.height)
x.get_older(2)
print(x.age)
print(x)

x2 = Person('Toto', 25, 175)
del x2

print(Person.amount)

# def helloWorld(self):
#     print('Hello World!')

# y = Person('Toto', 30, 180)
# y.helloWorld()


