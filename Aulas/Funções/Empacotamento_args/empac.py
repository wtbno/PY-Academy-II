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
    ...
