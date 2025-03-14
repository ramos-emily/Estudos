"""
Crie uma classe chamada Personagem que irá receber como construtor o nome completo,
altura, peso e resistência (0-100) do personagem, além disso, também crie um método
que se chame poder que conterá todos os atributos de instancia como privado não sendo
possível alterá-los, sendo estes: magia, persuasão, agilidade e forca, cada um avaliada de 0 a 100,
por fim, retorne apenas a soma de todos os pontos fornecidos. Crie 3 objetos personagens e
imprima o nome completo e quantidade de poder total do mais forte.
"""


class Personagem:  # Definição da Classe

    def __init__(self, nome_completo, altura, peso, resistencia):  # Método construtor
        # Declaração dos atributos do objeto
        self.nome_completo = nome_completo
        self.altura = altura
        self.peso = peso
        self.resistencia = resistencia

    def poder(self, magia, persuasao, agilidade, forca):  # Declaração do método de poder e de seus atributos
        self.__magia = magia
        self.__persuasao = persuasao
        self.__agilidade = agilidade
        self.__forca = forca
        return magia + persuasao + agilidade + forca  # Retona o
        # somatorio do
        # poder total


dict_poder = {}  # Dicionario que armazena todos os poderes com os
# personagens
kratos = Personagem('Kratos', 1.85, 90, 80)  # Criação do objeto kratos
dict_poder[kratos.nome_completo] = kratos.poder(100, 10, 80, 90)
# Armazena no dicionacio a chave como nome completo e como elemento o poder total
# print(f'{kratos._Personagem__magia}') #Mesmo executando já armazenando no dicionario, o atributo privado é criado

joel = Personagem('Joel Troy Baker', 1.80, 80, 60)  # Criação do objeto
# joel
dict_poder[joel.nome_completo] = joel.poder(0, 60, 60, 55)  # Armazena no
# dicionario

ezio = Personagem('Ezio Auditore da Firenze', 1.8, 85, 65)  # Criação do
# objeto ezio
dict_poder[ezio.nome_completo] = ezio.poder(0, 80, 80, 70)  # Armazena no
# dicionario

#print(kratos.__dict__)  # Retorna um dicionario com todos os atributos

maior = 0  # Armazena o valor do maior poder
nome = ''  # Armazena a chave do maior valor de poder
for chave, valor in dict_poder.items():  # A Ferramenta items() retorna
    # uma lista de tuplas de par
    # chave,valor
    if maior < valor:
        maior = valor
        nome = chave
print(f'O mais forte: {nome} com {maior} pontos de poder')
# Impressão do resultado final

