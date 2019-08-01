vetor = [30, 10, 40, 50, 20, 8]

print("Vetor original:", vetor)
print("Tamanho do vetor:", len(vetor))
print(" ")

# Contar as iterações/passos
for x in range(0, len(vetor)):
    # Fazer as verificações um a um no vetor inteiro
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