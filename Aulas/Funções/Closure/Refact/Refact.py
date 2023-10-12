def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

# => criação de uma função que cria outras funções


morning = criar_saudacao('Bom dia')
night = criar_saudacao('Boa noite')

# => array de nomes

for nome in ['Camila', 'Bruno', 'Thiago', 'Mayko', 'Ana', 'Nathalia']:
    print(morning(nome))
    print(night(nome))
