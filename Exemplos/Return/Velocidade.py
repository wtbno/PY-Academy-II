def velocidade(espaco, tempo):
    v = espaco/tempo
    return v
# Velocidade => nome da função espaço/tempo => args


print(velocidade(100, 20))
# Imprime o resultado da função
"""Ou ainda pode ser atribuida a uma variável"""
resultado = velocidade(100, 20)
print(resultado)
"""Atribuir a variável a uma nova base de cálculo"""
resultado = velocidade(100, 20)/20
print(resultado)
