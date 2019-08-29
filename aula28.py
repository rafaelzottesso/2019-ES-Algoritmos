def proc1():
    """
    Corpo do procedimento1 sem parâmetros
    """


def proc2():
    """
    Corpo do procedimento2 sem parâmetros
    """


def proc3(x, y):
    """
    Corpo do procedimento3 com parâmetros
    """


def proc4(msg):
    """
    Corpo do procedimento4 com parâmetros
    """


def exibirMensagem(vezes, nome):
    for i in range(vezes):
        print(nome)


def exibirVetor(v):
    for cont in range(len(v)):
        print(v[cont])


# Executando os procedimentos
x = "Zezinho"
exibirMensagem(3, x)
x = "Ayslan"
exibirMensagem(8, x)
x = "Algoritmos"
exibirMensagem(5, x)


# Executando outros procedimentos
vetor = [5, 4, 9, 10, 12]
lista = [10, 11, 12, 13, 14, 15, 16]
exibirVetor(vetor)
exibirVetor(lista)
