"""
Procedimentos com Parâmetros
Os parâmetros são valores/dados (adicionais) que são fornecidos
para um procedimento.
"""
import math
# Neste caso, o parâmetro é o valor 9
# Ele é necessário para que o procedimento sqtr() funcione corretamente conforme foi programado
r = math.sqrt(9)

# Neste procedimento, x é um parâmetro
def msg(x):
    print(x)

# Procedimento com mais parâmetros
def msg2(a, b, c):
    print(a)
    print(b)
    print(c)

# Usando o procedimento
#msg2(10, 22, 8)


# As variáveis v1, v2, v3 e soma
# Só existem no contexto (corpo) daquele procedimento
# São chamadas de variáveis locais
# Fora do procedimento elas não existem
def somar3(a, b, c):
    soma = a + b + c
    print("v1:", a)
    print("v2:", b)
    print("v3:", c)
    print("soma:", soma)
    a = 9

def somar2(a, b):
    soma = a + b
    print("Soma:", soma)    

a=int(input("Digite o 1. val:"))
b=int(input("Digite o 2. val:"))
c=int(input("Digite o 3. val:"))

somar3(a, b, c)

print("a:",a)
