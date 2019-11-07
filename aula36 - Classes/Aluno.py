from Data import Data

class Aluno:
    # Atributos
    nome = "" # String faz parte da linguagem
    idade = 0 # int faz parte
    status = False # booleano faz parte

    # Vamos usar um atributi do tipo que nós criamos
    dataNasc = Data() # Data não faz parte

    # Método Construtor
    def __init__(self):
        # self busca o que tem dentro dessa classe
        self.dataNasc = Data()