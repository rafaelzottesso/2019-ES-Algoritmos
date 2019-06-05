# Criação de vetores
v1 = [1, 2, 3, 8, 4, 9, 0]
v2 = [0]*6
v3 = [0]*10

# Verificando o tamanho de cada um
print("Tamanho do v1:", len(v1))
print("Tamanho do v2:", len(v2))
print("Tamanho do v3:", len(v3))

# Alterando/inserindo um valor armazenado no vetor
v1[1] = int(input("Digite um número: "))
v2[3] = 8

# Preenchendo um vetor
print("\n===== V3 =====")
i = 0
while( i < len(v3) ):
    v3[i] = int(input("Digite um número: "))
    i = i + 1

# Listando os valores de um vetor
print("\n===== V3 =====")
i = 0
while( i < len(v3) ):
    print("Na posição", i, "tem o valor", v3[i])
    i = i + 1
