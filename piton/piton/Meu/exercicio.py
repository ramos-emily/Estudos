#primeira letra maiuscula e estilo camelcase
# @staticmethod é pra nao precisar modificar as instancias da classe
# @classmethod para acessar ou modificar parametro da classe
# as underlines sao para deixar privadas ao inves de publicas

#class NomeDela:
    #conteudo dela

# class Animal:
#     pass

# leao = Animal()
# macaco = Animal()
# print(type(leao))
# print(type(macaco))

# class Carro:

#     def __init__(self, portas, cor):
#         self.portas = portas #publico
#         self.__arcondicionado = True #privado

# carroPai = Carro(4, 'prata')
# print(carroPai.portas)


# class Sapato:
#     qtdd = 7

#     def __init__(self, cor, tamanho, preco, qtddComprada):
#         self.preco = preco
#         self.qtddComprada = qtddComprada
#         self.cor = cor
#         self.tamanho = tamanho

# tamanco = Sapato(cor='azul', tamanho=42, preco=1200, qtddComprada=10)
# print(tamanco.preco)

# class Myclass:
#     @classmethod
#     def class_method(cls, x, y):
#         return
    
# result = Myclass.class_method(x=3, y=5)
# print(result)


# Crie uma classe chamada Personagem que irá receber como construtor o nome completo,
# altura, peso e resistência (0-100) do personagem, além disso, também crie um método
# que se chame poder que conterá todos os atributos de instancia como privado não sendo
# possível alterá-los, sendo estes: magia, persuasão, agilidade e forca, cada um avaliada de 0 a 100,
# por fim, retorne apenas a soma de todos os pontos fornecidos. Crie 3 objetos personagens e
# imprima o nome completo e quantidade de poder total do mais forte.
# """




class Personagem:
    
    def __init__(self, nome, altura, peso, resistencia):
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.resistencia = resistencia

naofuncionavei = Personagem(nome='bob Esponja', altura=1.50, peso=1, resistencia=0)
print(vars(naofuncionavei))
        
        
# class Poder:
    
#     def __init__(self, magia, persuasao, agilidade, forca):
#         self.magia = magia
#         self.persuasao = persuasao
#         self.agilidade = agilidade
#         self.forca = forca



print("so um commit aqui")







