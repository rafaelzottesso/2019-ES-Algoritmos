"""
-- Estrutura básica do laço de repetição while --

variável de controle iniciada
while(condição):
    .
    .
    .
    incremento da variável de controle

"""

# Variável de controle iniciada
cont = 1
# Condição do while montada de acordo com a variável de controle
while( cont <= 1000 ):
    # Código a ser processado
    print("Valor de cont:", cont)

    # Dentro do while pode ter qualquer coisa...
    # Pedir coisa para usuário, if, elif, else, etc
    # inclusive outro while :ooo

    # Alteração/incremento no valor da variável de contrle
    cont = cont + 1
    # Fim do while
    

# Continuação do programa, independente do resultado do while
print("Fora do while!")
