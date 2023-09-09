import tkinter as tk


def atualizar_visao(valor):
    visor.config(text=valor)


def calcular():
    expressao = visor.cget("text")
    try:
        resultado = eval(expressao)
        atualizar_visao(resultado)
    except Exception as e:
        atualizar_visao("Erro")


janela = tk.Tk()
janela.title("Calculadora ")


# Criação do visor
visor = tk.Label(janela, text="", font=("Arial", 20))
visor.grid()


botoes = ['7', '8', '9', '/',
          '4', '5', '6', '*',
          '1', '2', '3', '-',
          '0', '.', '=', '+', 'C']

linha = 1
coluna = 0

for texto in botoes:
    if texto == "=":
        botao = tk.Button(janela, text=texto, padx=20,
                          pady=20, command=calcular)
    else:
        botao = tk.Button(janela, text=texto, padx=20, pady=20,
                          command=lambda t=texto: atualizar_visao(visor.cget("text") + t))
    botao.grid(row=linha, column=coluna)
    coluna += 1
    if coluna > 4:
        coluna = 0
        linha += 1

janela.mainloop()
