"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""


# def Print(a, b, c): => seria um parâmetro
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')

# def imprimir(a, b, c):
#     print(a, b, c)


# imprimir(1, 2, 3) => argumentos da variável, ou valores
# imprimir(4, 5, 6)
# None é como se fosse um false


def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')


saudacao('Bruno')
saudacao('Camila')
saudacao('Shen')
saudacao()  # => caso esteja sem valor ele irá retornar o 'Sem nome' que está definido acima
"""
Funções podem usar parâmetros para receber valores. Parâmetro é o nome da "variável" dentro dos parênteses, argumento é o valor passado para o parâmetro no momento da execução da função.


"""
