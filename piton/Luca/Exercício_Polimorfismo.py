""""""
"""
1 - Crie uma superclasse chamada 'FormaGeometrica', que possui um método 'calcula_area' e recebe 
o nome de uma figura geométrica em seu método construtor. Após isso, crie duas subclasses 
('Areaquadrado' e 'Areacirculo') que herdam de 'FormaGeométrica' e calculam a área de sua respectiva 
forma. O método nas Classes Filhas deve ter o nome 'calcula_area', igual em sua Classe Mãe.

# 1

import math

class FormaGeometrica:
    def __init__(self, figura):
        self.__figura = figura

    def calcula_area(self):
        if self.__figura == 'quadrado':
            print(f"Área do quadrado: {float(input('Lado do quadrado: ')) ** 2} m²")
        elif self.__figura == 'circulo':
            print(f"Área do circulo: {(float(input('Raio do circulo: ')) ** 2) * math.pi} m²")


class Areaquadrado(FormaGeometrica):
    def calcula_areaa(self):
        print(f"Área: {float(input('Lado do quadrado: ')) ** 2} m²")


class Areacirculo(FormaGeometrica):
    def calcula_areaa(self):
        print(f"Área: {(float(input('Raio do circulo: ')) ** 2) * math.pi} m²")


quadrado = Areaquadrado('quadrado')
quadrado.calcula_area()

circulo = Areacirculo('circulo')
circulo.calcula_area()
"""