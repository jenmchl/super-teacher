from random import randint

class Student:
    def __init__(self, name, group):
        self.name = name
        self.id = randint(10000, 99999)
        self.group = group

    def printData(self):
        print('   ' + str(self.id ) + ' |   ' + self.group + '   | ' + self.name)
