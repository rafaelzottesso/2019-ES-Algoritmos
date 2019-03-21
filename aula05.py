# Entrada da idade
idade = input("Digite sua idade: ")
# Conversão de valores
idade = int(idade)

# Verifica a idade conforme as condições abaixo
if( idade < 0 ):
    print("Idade inválida!")
elif( idade < 3 ):
    print("Bebê detectado!")
elif( idade <= 12 ):
    print("Criança!")
elif( idade < 18 ):
    print("Adolescente!")
elif( idade < 60 ):
    print("Adulto!")
else:
    print("Melhor idade :D")

"""
Com "elif" podemos fazer o programa verificar
mais de uma condição para encontrar a verdadeira.
Porém, somente UM bloco de comandos será executado.
Este bloco pertence a primeira condição verdadeira encontrada.
Então, a ordem das condições que você montar vão influenciar
na execução do programa.
"""

# Operadores lógicos
"""
AND -> E
(condição) and (condição)
    V       e      V
As duas condições tem que ser True para o if/elif ser executado.

OR -> OU
(condição) or (condição)
Apenas UMA das duas tem que ser True.
O if/elif só não será executado se as duas condições forem Falsas.

NOT -> NÃO
not (condição)
Altera o valor lógico atual. Se a condição for True vira False.
Se for False vira True.
"""

x = 10
y = 20

if( x > 10 and x < 20 ):
    print("Condição verdadeira!")
else:
    print("A condição foi falsa.")
