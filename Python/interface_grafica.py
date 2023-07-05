# Ensina como fazer uma interface grafica usando TKINTE

import requests
from tkinter import * # isso importará todos os codigos que estão dentro do TKINTER por isso usamos o sinal (*) no final.


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

# Chama o texto_cotação do tkinter e cola ele igual a texto
    texto_cotações["text"] = texto

janela = Tk()

# Muda o titulo do programa por isso usamos o title.
janela.title("cotação atual das moedas")

# Se querermos aumentar a nossa janela vamos usar o metodo (geometry)
janela.geometry("300x200")
# Coloca texto na Janela por isso usamos o Label
texto_orientação = Label(janela, text="Clique no botão para ver a cotação da moeda")

# Escolher a posição do texto usamos o grid e depois dizemos qual é a coluna e a linha.
texto_orientação.grid(column=0, row=0, padx=10, pady=10) #se querermos colocar um outro texto abaixo do primeiro é so mudar o numero de linha e deixar a coluna igual do primeiro.

# Quando queremos adicionar um botão precisamos chamar o Button e dizer em qual tela ou janela ela esta, também devemos colocar no botão o que as pessoas devem fazer então para isso usamos o (Command=) e diz para ele o nome de uma função sem parenteses.
botão = Button(janela, text="Buscar cotação do Dólar/Euro/BTC", command=pegar_cotacoes)

# Quando criamos o botão devemos dizer em que coluna e linha deve estar ou seja deve estar dentro do grid.
botão.grid(column=0, row=1, padx=10, pady=10) # Para dar espaço nos elementos usamos (padx e pady) que significa pading

# Onde vai aparecer as cotações
texto_cotações = Label(janela, text="")

# Usamos o grid também para indicar onde estará.
texto_cotações.grid(column=0, row=2, padx=10, pady=10)


janela.mainloop()