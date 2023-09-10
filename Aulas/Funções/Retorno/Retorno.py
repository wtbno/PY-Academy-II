"""
Retorno de valores das funções (return)]
# Existem dois tipos de funções:
    => Que executam ações como p.ex: print(variavel)

    return de dentro de uma função, significa que sua função irá retornar algum valor para utilziar em var p.ex:
    ***print != return***

return é utilizado em funções e métodos, e após utilizar o return sinaliza o python para parar tudo que está sendo executado e realizar a função do return. Não é porssível executar algo após o return
"""
# variavel = print("Bruno")


def soma(x, y):
    if x > 10:
        return 10
    return x + y
    # Não executável após o return print(soma)


soma1 = soma(1, 7)
soma2 = soma(1, 5)
print(soma1 + soma2)
