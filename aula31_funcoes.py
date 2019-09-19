# Importa a biblioteca math
import math

# Cria uma função "f" que possui um parâmetro e tem retorno.
# Sempre que temos uma função, temos retorno.
# Basta usar a palavra "return" seguida do que você quer devolver para quem chamou/executou a função
def f(x):
    m = int(x/2) + 1
    return m

# Função "g" com dois parâmetros e retorno
def g(a, b):
    v = (math.sqrt(a) + b) / f(b)
    return v

# Procedimento "h" porque não tem retorno.
def h():
    x1 = int(input("Informe um numero: "))
    x2 = int(input("Informe um numero: "))
    print("Resultado: ", g(x1, x2) )

