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
