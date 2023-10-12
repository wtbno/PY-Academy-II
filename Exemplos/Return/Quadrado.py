"""para declarar uma função, usa-se uma palavra reservada representada por def e o que a função retorna para o programa é realizado através da palavra reservada return. O formato de uma função tem a forma:"""


def quadrado(numero):
    resultado = numero ** 2
    return resultado


numero = 5
resultado_quadrado = quadrado(numero)
print(resultado_quadrado)


def funcao1(x, y, z=2):
    if z > 1:
        return z * (x + y)
    else:
        return z / (x + y)


print(funcao1)
