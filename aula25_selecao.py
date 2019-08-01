vetor = [30, 10, 40, 50, 20, 8]

print("Vetor original:", vetor)
print("Tamanho do vetor:", len(vetor))
print(" ")

# Ocupar a posição do vetor que procura-se o menor para ele
for x in range(0, len(vetor)-1):
    menor = x
    # Fazer as verificações no vetor do x em diante
    for y in range(x+1, len(vetor)):

        print("Comparando {}(Pos: {}) com {}(Pos: {}).".format(vetor[x], x, vetor[y], y))

        if(vetor[menor] > vetor[y]):
            menor = y
            print("Achou menor")
        else:
            print("Não é menor")

    # Depois de comparar todos da posição "y", faz a troca se o valor da variável "menor" foi alterado
    if (menor != x):
        aux = vetor[x]
        vetor[x] = vetor[menor]
        vetor[menor] = aux
        print("\nFez a troca...")

    print("\nVetor:", vetor)
    # Se não quiser que o algoritmo fique parando, comente a linha abaixo
    input("Aperte ENTER para continuar...\n")

print("Vetor ordenado:", vetor)


"""
# Links úteis #
https://www.hackerearth.com/pt-br/practice/algorithms/sorting/selection-sort/visualize/
https://visualgo.net/bn/sorting
"""
