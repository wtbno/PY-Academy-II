def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar


saud = criar_saudacao('Bom dia', 'Bruno')
saud_2 = criar_saudacao('Boa noite', 'Camila')


print(saud())
print(saud_2())
"""
print(saud)
print(saud_2)

Agora, estamos imprimindo as próprias funções saud e saud_2, não os resultados de chamadas dessas funções.

Portanto, ao imprimir saud e saud_2, você verá algo como <function criar_saudacao.<locals>.saudar at 0x...>. Isso representa o objeto da função, não o resultado da chamada da função.

Os valores passados para saudacao e nome quando você chama criar_saudacao são armazenados nas funções internas saudar. Essas funções internas formam closures, o que significa que elas têm acesso aos valores dos parâmetros da função externa (criar_saudacao).

Então, quando você chama saud() e saud_2(), essas funções internas estão usando os valores fornecidos anteriormente. Para saud, você terá 'Bom dia, Bruno!' e para saud_2, você terá 'Boa noite, Camila!'. Isso ilustra a capacidade de funções internas em Python de "lembrar" os valores dos argumentos da função externa mesmo após a função externa ter sido concluída.

"""
