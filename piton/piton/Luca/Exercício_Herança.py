""""""
"""
1 - Desenvolva o sistema de um controle universal para uma casa. O controle deve ser a Classe-Mãe, que 
contém o método liga/desliga e é herdada por outras três classes (equipamentos controlados): 
ar-condicionado, micro-ondas e televisão, que controlam, respectivamente, temperatura, tempo e volume em 
métodos dentro das classes. Além disso, os métodos construtores das Classes Filhas recebem a variável 
controlada em seu valor atual, por exemplo 'temperaturaAtual'. 
Obs.: Utilize também propriedades para realizar o acesso aos atributos.


# 1


class Controle:

    ligado = False
    def liga_desliga(self):
        self.ligado = not self.ligado

class Arcondicionado(Controle):

    def __init__(self, temperaturaAtual):
        self.__temperaturaAtual = temperaturaAtual

    def controle_temperatura(self, temperatura):
        self.__temperaturaAtual = temperatura

    @property
    def temperaturaAtual(self):
        return f'Temperatura atual: {self.__temperaturaAtual}'


class Microondas(Controle):

    def __init__(self, tempoAtual):
        self.__tempoAtual = tempoAtual

    def controle_tempo(self, tempo):
        self.__tempoAtual = tempo

    @property
    def tempoAtual(self):
        return f'Tempo atual: {self.__tempoAtual}'


class Televisao(Controle):

    def __init__(self, volumeAtual):
        self.__volumeAtual = volumeAtual

    def controle_volume(self, volume):
        self.__volumeAtual = volume

    @property
    def volumeAtual(self):
        return f'Volume atual: {self.__volumeAtual}'


arc = Arcondicionado(45)
mic = Microondas(60)
tv = Televisao(85)

print(arc.ligado)
arc.liga_desliga()
print(arc.ligado)
print(arc.temperaturaAtual)
arc.controle_temperatura(35)
print(arc.temperaturaAtual)

print('\n')
print(mic.ligado)
mic.liga_desliga()
print(mic.ligado)
print(mic.tempoAtual)
mic.controle_tempo(40)
print(mic.tempoAtual)

print('\n')
print(tv.ligado)
tv.liga_desliga()
print(tv.ligado)
print(tv.volumeAtual)
tv.controle_volume(100)
print(tv.volumeAtual)
"""