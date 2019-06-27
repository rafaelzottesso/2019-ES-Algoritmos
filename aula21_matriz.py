vet = [ [1, 2, 3], [8, 9, 10], [0, 0, -5] ]

print("Quantidade de linhas:", len(vet))
print("Quantidade de colunas:", len(vet[0]))

print("Desenho da matriz:", vet)

# Um laço de repetição para percorrer as linhas
for lin in range( 0, len(vet) ):

    # print("Linha", lin , "-->", vet[lin])

    # Um laço para percorrer as colunas de cada linha
    for col in range( 0, len( vet[lin] ) ):

        # Imprimir o valor na linha "i" e coluna "j"
        print( vet[lin][col] )


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

# Criando uma matriz com tamanho customizado
linhas = 3  # define a quantidade de linhas
colunas = 3 # define a quantidade de colunas
matriz = [] # cria um vetor vazio

# Para cada linha da matriz que queremos criar...
for i in range(0, linhas):
    # Adiciona a quantidade de colunas informada
    # m.append() adicona alguma coisa no final de "m"
    matriz.append( [0] * colunas )

# Plus!!
# Documentação com mais funções prontas para trabalhar com listas/vetores
# https://docs.python.org/3/tutorial/datastructures.html

# Para cada linha...
for linha in range(0, len(matriz)):
    # Para cada coluna dentro de cada linha
    for coluna in range(0, len(matriz[linha])):
        # Armazena um número na matriz de acordo com a "linha" e "coluna" definida no for
        valor = int(input("Informe valor para a linha {} e coluna {}: ".format(linha, coluna)))
        # O input pode ser feito direto na matriz, aqui ficou separado por causa do tamanho da projeção
        matriz[linha][coluna] = valor
        # x = int(input("Informe valor para a linha {} e coluna {}:".format(linha, coluna)))

print(matriz)

