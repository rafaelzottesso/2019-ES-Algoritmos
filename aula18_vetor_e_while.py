x = int(input("Tamanho: "))
vetor = [0] * x

# Exemplo com valores do próprio programa
pos = 0
while( pos < len(vetor) ):
    vetor[pos] = pos + 1
    pos = pos + 1

print(vetor)
# Exemplo com usuário Preenchendo os valores do vetor
# pos = 0
# while( pos < len(vetor) ):
#     vetor[pos] = int(input("Número: "))
#
#     pos = pos + 1

# Percorrer o vetor em ordem inversa
pos = len(vetor) - 1
while( pos >= 0 ):
    print("Posição", pos, "valor", vetor[pos])
    pos = pos - 1

print("\nUsando for...")
for pos in range(len(vetor)):
    print("Posição", pos, "valor", vetor[pos])




#
