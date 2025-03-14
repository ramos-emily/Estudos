""""""
"""
1 - Crie duas classes (uma para um personagem no video game e outra para o controle do console). 
O controle deve ser capaz de fazer o personagem pular, abaixar, desviar para esquerda e desviar 
para direita, sendo comandado, respectivamente, pelas teclas W, A, S e D. Use a dica e a função choice() 
para determinar por onde virá o obstáculo ('Cima', 'Baixo', 'Esquerda' ou 'Direita'), e o tempo para 
o próximo obstáculo, que deve decair com o aumento dos pontos. Cada obstáculo passado gera +1 ponto. 
Ainda, crie um loop infinito do jogo até a pessoa perder. Por fim, apresente a pontuação final.

Dica:
import time
time.sleep(3) # O programa 'para' por 3 segundos


# 1

class Personagem:

    def __pular(self):
        print('PULOU')

    def apertou_w(self, personagem):
        personagem.__pular()

    def __abaixar(self):
        print('ABAIXOU')

    def apertou_s(self, personagem):
        personagem.__abaixar()

    def __desviar_esquerda(self):
        print('DESVIOU PARA ESQUERDA')

    def apertou_a(self, personagem):
        personagem.__desviar_esquerda()

    def __desviar_direita(self):
        print('DESVIOU PARA DIREITA')

    def apertou_d(self, personagem):
        personagem.__desviar_direita()


class Teclado:

    def tecla_w(self, personagem):
        personagem.apertou_w(personagem)

    def tecla_s(self, personagem):
        personagem.apertou_s(personagem)

    def tecla_a(self, personagem):
        personagem.apertou_a(personagem)

    def tecla_d(self, personagem):
        personagem.apertou_d(personagem)


import time
from random import choice as ch

vivo = True
obstaculos = ['Cima', 'Baixo', 'Esquerda', 'Direita']

pontos = -1
tempo = 2

teclado = Teclado()
bob = Personagem()

while vivo:
    passou = False
    pontos += 1
    time.sleep(tempo - pontos / 10)
    print('\n')
    obstaculo = ch(obstaculos)
    print(f'Obstáculo: {obstaculo}')
    comando = input('Comando: ')
    if comando == 'w' and obstaculo == 'Baixo':
        teclado.tecla_w(bob)
        passou = True
    elif comando == 's' and obstaculo == 'Cima':
        teclado.tecla_s(bob)
        passou = True
    elif comando == 'a' and obstaculo == 'Direita':
        teclado.tecla_a(bob)
        passou = True
    elif comando == 'd' and obstaculo == 'Esquerda':
        teclado.tecla_d(bob)
        passou = True
    else:
        vivo = False

print('\n')
print('GAME OVER!')
print('Obrigado por jogar...')
print(f'Pontuação: {pontos}')
"""