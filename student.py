class Student:
    def __init__(self, name, number, group):
        self.name = name
        self.number = number
        self.group = group

    def printData(self):
        print('Dados de ', self.name)
        print('Número: ', self.number, ' | ', 'Turma: ', self.group)
