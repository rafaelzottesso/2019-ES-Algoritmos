vetor = [30, 10, 40, 50, 20, 8]

print("Vetor original:", vetor)
print("Tamanho do vetor:", len(vetor))
print(" ")

# Ocupar as posições do vetor
for x in range(0, len(vetor)):
    # Fazer as verificações a partir da posição x+1 porque o x já está lá no for anterior
    for y in range(x+1, len(vetor)):

        print("Comparando {}(Pos: {}) com {}(Pos: {}).".format(vetor[x], x, vetor[y], y))

        if(vetor[x] > vetor[y]):
            aux = vetor[x]
            vetor[x] = vetor[y]
            vetor[y] = aux
            print("Trocou")
        else:
            print("Não trocou")

        print("Vetor:", vetor)
        # Se não quiser que o algoritmo fique parando, comente a linha abaixo
        input("Aperte ENTER para continuar...\n")

print("Vetor ordenado:", vetor)


"""
# Links úteis #
https://www.hackerearth.com/pt-br/practice/algorithms/sorting/insertion-sort/visualize/
https://visualgo.net/bn/sorting
https://www.advanced-ict.info/interactive/algorithms.html
"""
