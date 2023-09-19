"""
args => argumentos não nomeados

* - *args(empacotamento e desempacotamento)


Em Python, o termo *args (com um asterisco antes de "args") é usado para passar um número variável de argumentos posicionais para uma função. Isso permite que você crie funções que aceitem qualquer número de argumentos posicionais sem a necessidade de definir explicitamente quantos argumentos serão passados.

Aqui está como funciona:

Quando você coloca *args como um parâmetro de uma função, está indicando que a função pode receber zero ou mais argumentos posicionais.

Dentro da função, args se torna uma tupla que contém todos os argumentos posicionais passados para a função.

Você pode acessar os valores individuais da tupla args usando indexação, como faria com qualquer outra tupla.

Aqui está um exemplo simples de como usar *args em uma função:


def minha_funcao(*args):
    for arg in args:
        print(arg)

minha_funcao(1, 2, 3, "Hello")


"""

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)


def soma(*args):
    total = 0
    for numero in args:

        total += numero  # acumulador

    return total
    ...


# Acumulador soma ele mesmo mais um valor
# print(args, type(args))  # mostra o resultado de uma tupla


soma1 = soma(1, 2, 3)
print(soma1)
soma2 = soma(4, 5, 6)
print(soma2)
numeros = (56, 89, 31, 87, 6, 48, 21, 1, 11, 39)
soma3 = soma(*numeros)
print(soma3)


# função sum recebe vários argumentos como tuplas, ou somente dois diretos
# print(sum((56, 89, 31, 87, 6, 48, 21, 1, 11, 39)))
