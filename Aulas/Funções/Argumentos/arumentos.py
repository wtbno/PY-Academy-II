"""
=> Args nomeados e não nomeados em Python

* Args nomeados possuem o nome atribuido ao sinal de igual "="
* Args não nomeados recebem apenas o argumento (valor)


"""


def soma(x, y, z):
    # def => definição de função
    # soma => nome da função, o que é alocado na memória
    # (x, y, z) => execução da função
    # Parâmetro se utiliza na definição da função, que é o nome das váriaveis na def da função
    # Definição
    print(f'{x= }  {y= } {z= }', '|', 'x + y + z = ', x+y+z)


soma(1, 2, 300)  # => Args não nomeados ou posicionais
soma(y=2, x=1, z=300)  # => args nomeado
# É uma boa prática ou usar args nomeado ou não nomeados de forma separada
# Argumento é o valor que é preenchido nos parâmetros acima
# Valores (Argumentos posicional)
# Se inserir um parâmetro sem args, irá estourar o seguinte erro: "TypeError: soma() missing 1 required positional argument: 'z'"

# É interessante usar argumentos nomeados para poder alterar a ordem no envio de valores para a função
# Não pode enviar args posicionais apos args nomeados
