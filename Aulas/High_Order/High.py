def saudacao(msg):
    return (msg)


def executa(funcao, texto):
    return funcao(texto)


"""
A função executa é projetada para ser genérica e aceitar qualquer função como argumento. Ela fornece uma maneira flexível de executar uma função com um determinado conjunto de argumentos. Isso pode ser útil em situações em que você deseja passar diferentes funções como argumentos para uma função principal.

=> Higher Order Functions - Funções que podem receber e/ou retornar outras funções

=> First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)


"""

v = executa(saudacao, "Bom dia")
print(v)
