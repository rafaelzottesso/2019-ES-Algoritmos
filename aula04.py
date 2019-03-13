x = 10
y = 20

"""
> maior
< menor
>= maior ou igual
<= menor ou igual
== igual
!= diferente

Numa estrutura condicional, apenas um bloco de comando é executado. Os demais
são ignorados. Este bloco a ser executado está diretamente ligado com a condição
definida e ela precisa ser verdadeira.
"""

if(x>=y):
    # Este conteúdo será executado se a condição da linha anterior for verdadeira
    print("O valor de X é maior ou igual!")
else:
    # Se a condição anterior for falsa, este conteúdo será executado
    print("O valor de Y é maior!")


"""
Uso do print com a função "".format()

"""

nome = "Rafael"
email = "rafael.zottesso@ifpr.edu.br"
idade = 31

print("Olá", nome, ". Seu email é", email," e sua idade é", idade, ".")

print("Olá {}. Seu email é {} e sua idade é {}.".format(nome, email, idade ) )
