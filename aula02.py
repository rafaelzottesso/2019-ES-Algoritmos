# Toda entrada do input é STR (string)
idade = input("Digite sua idade: ")

# Posso converter de STR para INT ou FLOAT
idade = float(idade)
# Realiza as operações matemáticas
metade = (idade / 2)

# Mostrando o resultado
print("A metade é", metade)

print("""
Operadores matemáticos (ordem de prioridade):
**  - Potência
*   - Multiplicação
/   - Divisão
+   - Soma
-   - Subtração
""")

print("Raiz quadrada: x ** (1/2)")
print("Raiz cúbica: x ** (1/3)")

print("Coloque no lugar do N o grau da raiz:")
print("Raiz N: x ** (1/N)")

print("""
Variáveis:
- podem ter letras, números e _ (underline)
- devem começar com letras ou _
- não pode ter espaço ou outros caracteres especiais
- "a" é diferente de "A"
- não usar palavras reservadas da linguagem
- preferencialmene com a primeira letra minúscula
""")

# Temos aqui três variáveis diferentes
nomecompleto = "Rafael"
nome_completo = "Rafael"
nomeCompleto = "Rafael"
