# Criação de vetores
v1 = [1, 2, 3, 8, 4, 9, 0]
v2 = [0]*6

# Verificando o tamanho de cada um
print("Tamanho do v1:", len(v1))
print("Tamanho do v2:", len(v2))

# Alterando/inserindo um valor armazenado no vetor
v1[1] = int(input("Digite um número: "))
v2[3] = 8

# Percorrendo um vetor
print("\n===== V1 =====")
i = 0
while( i < len(v1) ):
    print("Na posição", i, "tem o valor", v1[i])
    i = i + 1

print("\n===== V2 =====")
i = 0
while( i < len(v2) ):
    print("Na posição", i, "tem o valor", v2[i])
    i = i + 1
