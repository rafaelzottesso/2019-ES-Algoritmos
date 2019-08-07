"""
Introdução a Procedimentos (blocos de instruções)

'x' --> Isso é uma string
x   --> Variável
x() --> Procedimento

print() --> É um procedimento
"""
def nome_do_procedimento():
    # Aqui vai todo o bloco de instruções
    print("Iniciando procedimento...")    

def pedeMostra():
    x = int( input("Número: ") )
    print("Você digitou:", x)

def exibirMenu():
    print("""
        ** Menu Principal **
        1. Inserir
        2. Alterar
        3. Excluir
        4. Sair
    """)


####################################
exibirMenu()

pedeMostra()
#pedeMostra()
#pedeMostra()
