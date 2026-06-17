class Aluno:
    def __init__(self,nome,CPF,matricula,mae,contato):
        self.nome = nome
        self.CPF = CPF
        self.matricula = matricula
        self.mae = mae
        self.contato = contato

    def exibir_aluno(self):
            print(f'Nome: {self.nome} \nCPF: {self.CPF} \nMatricula: {self.matricula} \nMae: {self.mae} \ncontato: {self.contato}')


alunos = []

aluno1 = Aluno("Ana Beatriz", "123.456.789-00", "2026001", "Dona Maria", "(81) 99999-0000")
alunos.append(aluno1)
aluno2 = Aluno("Carlos Eduardo", "987.654.321-11", "2026002", "Dona Joana", "(81) 98888-1111")
alunos.append(aluno2)


aluno2.exibir_aluno()