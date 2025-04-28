import requests 
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()

def moeda():
    print("[1]Dólar\n[2]Euro\n[3]Bitcoin")
    escolha = int(input("escolha a moeda: "))
    if escolha == 1:
        cotacoes_dolar = cotacoes['USDBRL'] ['bid']
        print(cotacoes_dolar)
    elif escolha == 2:
        cotacoes_euro = cotacoes['EURBRL'] ['bid']
        print(cotacoes_euro)
    elif escolha == 3:
        cotacoes_bitcoin = cotacoes['BTCBRL'] ['bid']
        print(cotacoes_bitcoin)
    else:
        print("nao funcionou vei")

moeda()


