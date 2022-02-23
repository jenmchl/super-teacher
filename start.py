from student import Student

def register_student():
    print("  ------------ Cadastro de Aluno ------------")
    nameInput = input("  Nome: ")
    groupInput = input("  Turma: ")

    new_student = Student(nameInput, groupInput)
    all_students.append(new_student)
    print('  ID do aluno criado: ', new_student.id)

print('')
print("------------ Super Teacher ------------")

all_students = []

operation = "0"
while operation != "4":
    print('')
    print("|------------ Menu ------------|")
    print('| [1] Cadastrar Aluno          |')
    print('| [2] Mostrar lista de Alunos  |')
    print('| [3] Inserir Avaliação        |')
    print('| [4] Sair do Programa         |')
    print("|------------------------------|")

    operation = input('Escolha uma opção: ')
    print('')

    if operation == "1":
        register_student()

    if operation == "2":
        print('  -- LISTA DE ALUNOS --')
        print('')
        print('  Número | Turma | Nome ')
        for student in all_students:
            student.printData()

    if operation == "3":
        print('Não disponível')

print("Programa Encerrado")
