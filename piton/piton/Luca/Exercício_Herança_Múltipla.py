""""""
"""
1 - Crie duas classes chamadas 'Homem' e 'Urso', que recebem apenas nome como parâmetro. Estas classes 
devem herdar de outras duas chamadas 'Carnivoros' e 'Herbivoros', que possuem dois métodos cada 
('caçar_animal' e 'comer_carne' para 'Carnivoros', 'procurar_arvore' e 'comer_folhas' para 'Herbivoros') 
e herdam de uma Superclasse chamada 'Animal', na qual possui os métodos 'andar' e 'correr'. Por fim, 
instancie dois objetos, da classe 'Homem' e da classe 'Urso', e execute todos os métodos.

Obs.: Crie um método para as classes 'Homem' e 'Urso' representando uma ação característica de cada, 
por exemplo ler um livro para o homem e hibernar para o urso.

# 1

class Animal:
    def andar(self):
        print('Andando...')

    def correr(self):
        print('Correndo...')


class Carnivoros(Animal):
    def cacar_animal(self):
        print('Caçando animal...')

    def comer_carne(self):
        print('Comendo carne...')


class Herbivoros(Animal):
    def procurar_arvore(self):
        print('Procurando árvore...')

    def comer_folhas(self):
        print('Comendo folhas...')


class Homem(Carnivoros, Herbivoros):
    def __init__(self, nome):
        self.__nome = nome

    def lendo_livro(self):
        print('Lendo um livro...')


class Urso(Carnivoros, Herbivoros):
    def __init__(self, nome):
        self.__nome = nome

    def hibernar(self):
        print('Hibernando...')


andre = Homem('André')
andre.lendo_livro()
andre.andar()
andre.procurar_arvore()
andre.correr()
andre.cacar_animal()
andre.comer_folhas()
andre.comer_carne()

print('\n')
ze = Urso('Zé Colmeia')
ze.hibernar()
ze.andar()
ze.procurar_arvore()
ze.correr()
ze.cacar_animal()
ze.comer_folhas()
ze.comer_carne()
"""