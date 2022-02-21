from student import Student

print("------------ Super Teacher ------------")

all_students = []

operation = "0"
while operation != "4":
    print('  [1] Cadastrar Aluno')
    print('  [2] Mostrar lista de Alunos')
    print('  [3] Inserir Avaliação')
    print('  [4] Sair do Programa')

    operation = input('Escolha uma opção: ')

    if operation == "1":
        print("------------ Cadastro de Aluno ------------")
        nameInput = input("Nome: ")
        numberInput = input("Número: ")
        groupInput = input("Turma: ")

        new_student = Student(nameInput, numberInput, groupInput)
        all_students.append(new_student)

    if operation == "2":
        for student in all_students:
            student.printData()


    if operation == "3":
        print("Funcionalidade não disponível!")

print("Programa Encerrado")        
