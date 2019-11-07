from Data import Data

def exibirData(d):
    print("{}/{}/{}".format(d.dia, d.mes, d.ano))

def obterTextoData(d):
    return "{}/{}/{}".format(d.dia, d.mes, d.ano)

dataNascimento = Data()

dataNascimento.dia = int(input("Dia de nascimento:"))
dataNascimento.mes = int(input("Mês de nascimento:"))
dataNascimento.ano = int(input("Ano de nascimento:"))

exibirData(dataNascimento)

print( obterTextoData(dataNascimento) )