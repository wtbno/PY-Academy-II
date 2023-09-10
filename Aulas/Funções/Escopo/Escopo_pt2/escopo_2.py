"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1

# Cada função tem seu próprio escopo
# De dentro para fora


def escopo_1():
    # global x  # Ao alterar a var dentro da execução da função é uma má prática
    x = 10
    # Para isso pode se passar o parâmetro e utiliza-lo como argumento

    def escopo_2():
        # global x
        x = 11
        y = 2
        print(x, y)

    escopo_2()
    print(x)


print(x)
escopo_1()
print(x)
