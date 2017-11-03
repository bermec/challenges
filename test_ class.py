import re

class test:

    DATA = 7


    def __init__(self, data):
        self.data = data

    def output(self):
        self.DATA += + 2
        return self.DATA

    def output2(self):
        self.data *= 2 + self.DATA
        return self.data

class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance


if __name__ == '__main__':

    var_test = test(2)
    print(var_test.output())
    print(var_test.output2())

    d = Dog('Fido')
    e = Dog('Buddy')
    d.kind  # shared by all dogs
    'canine'
    e.kind  # shared by all dogs
    'canine'
    d.name  # unique to d
    'Fido'
    e.name  # unique to e
    'Buddy'

