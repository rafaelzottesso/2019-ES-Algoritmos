vetor = [30, 10, 40, 50, 20, 8]

print("Vetor original:", vetor)
print("Tamanho do vetor:", len(vetor))
print(" ") 

# Contar as iterações/passos
for x in range(0, len(vetor)-1):
    # Fazer as verificações um a um no vetor inteiro
    for y in range(0, len(vetor)-1):

        print( "Comparando {}(Pos: {}) com {}(Pos: {}).".format(vetor[y], y, vetor[y+1], y+1) )

        if(vetor[y] > vetor[y+1]):
            aux = vetor[y]
            vetor[y] = vetor[y+1]
            vetor[y+1] = aux
            print("Trocou")
        else:
            print("Não trocou")

        print("Vetor:", vetor)
        # Se não quiser que o algoritmo fique parando, comente a linha abaixo
        input("Aperte ENTER para continuar...\n")

print("Vetor ordenado:", vetor)            

"""
# Links úteis #
https://www.hackerearth.com/pt-br/practice/algorithms/sorting/bubble-sort/visualize/
https://visualgo.net/bn/sorting?slide=1
https://www.advanced-ict.info/interactive/algorithms.html
"""
