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
