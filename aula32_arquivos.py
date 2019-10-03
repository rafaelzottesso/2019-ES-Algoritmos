"""
ARQUIVOS: conjunto de dados armazenados em disco.

Ações em arquivos:
- Abrir arquivo   
    open("nomearquivo.txt", modoAbertura)
        modos: "r" - read (apenas lê dados do arquivo)
               "w" - write (sempre "cria" um arquivo novo. Se ja existir, ele é "zerado")
               "a" - append (escreve no final de arquivo ja existente)
- Fechar arquivo
    varArquivo.close()
- Gravar dados no arquivo
    varArquivo.write("conteúdo")
- Ler os dados do arquivo
     
"""


"""
Criar um procedimento que receba
como parâmetro o nome de um arquivo.
O procedimento deverá:
- abrir o arquivo para atualização 
  (append), 
- solicitar um novo valor ao usuário 
  e salvar este nome no arquivo, 
- salvar uma quebra de linha,
- fechar o arquivo aberto.
"""
def escrever_nome(nome_arquivo):
    xuxu = open(nome_arquivo,"a")
    nome = input("Digite um nome para salvar:")
    xuxu.write(nome + "\n")
    xuxu.close()

"""
Crie um procedimento que receba
o nome de um arquivo como parâmetro e
abra o arquivo em modo leitura.
Leia o arquivo
Feche o arquivo
"""
def ler_arquivo(nome_arquivo):
    palmeirasNaoTemMundial = open(nome_arquivo, "r", encoding="utf-8")
    
    conteudo = palmeirasNaoTemMundial.readlines()
    
    palmeirasNaoTemMundial.close()

    for linha in range(0, len(conteudo)):
        print( conteudo[linha] , end="")


"""
Ayslan Trevizan Possebom|ayslan@ifpr.edu.br|52.000,00


Usamos a função split() de uma String para "quebrar" uma String
A String será transformada em um vetor.
Fornecemos o caractere usado para quebrar a String.
A instrução abaixo:
dados = stringqualquer.split("|")

Faz isso daqui automaticamente:
dados[0] = "Fulano de Tal"
dados[1] = "fulano@ifpr.edu.br"
dados[2] = "5000.90"
"""












"""
open("arquivo.txt", "r", encoding="utf-8")
"""
