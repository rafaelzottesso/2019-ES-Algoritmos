"""
-- Estrutura básica do laço de repetição while --

variável de controle iniciada
while(condição):
    .
    .
    .
    incremento da variável de controle

"""

# # Variável de controle iniciada
# cont = 1
# # Condição do while montada de acordo com a variável de controle
# while( cont <= 1000 ):
#     # Código a ser processado
#     print("Valor de cont:", cont)
#
#     # Dentro do while pode ter qualquer coisa...
#     # Pedir coisa para usuário, if, elif, else, etc
#     # inclusive outro while :ooo
#
#     # Alteração/incremento no valor da variável de contrle
#     cont = cont + 1
#     # Fim do while

# Fazendo o contador inverso...
cont = 5
while (cont >= 1):
    print(cont)
    cont = cont - 1

# Pedindo várias notas ao usuário
cont = 1 # inicia o contador
soma = 0 # inicia a variável de soma
while(cont <= 4):
    nota = int(input("Informe uma nota:"))
    soma = soma + nota # junta a soma atual com a nota
    cont = cont + 1 # aumenta o contador
# Por fim, faz esse print 1x só porque está fora do while
print("Média: ", soma/4)

# Continuação do programa, independente do resultado do while
print("Fora do while!")
