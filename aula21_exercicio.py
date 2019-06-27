# Criação da matriz
matriz = [ [1,2,3,4], [5,6,7,8], [9,10,11,12] ]

#percorrer a matriz toda
for linha in range(0, len(matriz)):
    for coluna in range(0, len(matriz[linha])):
        # \t da um "tab" no print
        # end="" diz que não vai quebrar a linha
        # quando terminar o print
        print(matriz[linha][coluna],"\t",end="")
    # Depois de terminar as colunas e ir para uma nova linha
    # É necessário fazer um print para começar uma linha nova
    print()

# Só para pular mais uma linha
print("-----------------------")

# Percorrendo somente a linha 2 dessa matriz
# Verificamos o tamanho somente da linha 2 pelo len(matriz[2])
for coluna in range(0, len(matriz[2])):
    # A linha sempre vai ser 2, o que muda é a coluna
    print(matriz[2][coluna])


# Percorrendo somente a coluna 2 da matriz
# Para isso, len(matriz) conta a quantidade de linhas
for linha in range(0, len(matriz)):
    # Mostra na tela todas as linhas na coluna 2
    print( matriz[linha][2] )