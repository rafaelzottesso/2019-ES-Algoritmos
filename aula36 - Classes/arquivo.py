from Aluno import Aluno

def exibirAluno(a):
    print("Aluno:")
    print("Nome: ", a.nome)
    print("Idade: ", a.idade)
    if(a.status == True):
        print("Status: Regular")
    else:
        print("Status: Não matriculado")
    print("{}/{}/{}".format(a.dataNasc.dia, a.dataNasc.mes, a.dataNasc.ano))

alu1 = Aluno()
alu1.nome = "Flávio"
alu1.idade = 19
alu1.status = True
alu1.dataNasc.dia = 6
alu1.dataNasc.mes = 6
alu1.dataNasc.ano = 2000

alu2 = Aluno()
alu2.nome = "Kelvin"
alu2.idade = 20
alu2.status = False
alu2.dataNasc.dia = 1
alu2.dataNasc.mes = 10
alu2.dataNasc.ano = 2010
alu2.dataNasc.horario.horas = 22
alu2.dataNasc.horario.minutos = 1
alu2.dataNasc.horario.segundos = 48

exibirAluno(alu1)
exibirAluno(alu2)
