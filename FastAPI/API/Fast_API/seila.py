import requests 
import json

conselho = requests.get("https://api.adviceslip.com/advice")
conselho = conselho.json()


def help ():
    print("--------------------------")
    print("I HAVE A ADIVICE FOR YOU")
    print("--------------------------")
    resp = input("VOCÊ QUER? s/n: ")
    if resp == 's':
        pravoce = conselho['slip']['advice']
        print(pravoce)
    elif resp == 'n':
        print("entao vai se lascar")
    else:
        print("s ou n, por favor")


help()

print("testando git aqui")

