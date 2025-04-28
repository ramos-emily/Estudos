# class Personagem:

#     def __init__(self, nome, altura, peso, resistencia):
#         self.nome = nome
#         self.altura = altura
#         self.peso = peso
#         self.resistencia = resistencia

# personagem1 = Personagem(nome='Luca', altura=1.85, peso=75, resistencia=100)
# print(personagem1)



class Cadastro():
    def __init__(self, nome, idade, sexo, CEP):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.CEP = CEP

    def maior_idade(self, idade):
        if (idade < 18):
            print("De menor")
        else:
            print("")

    def sexo(self, sexo, nome):
        if (sexo == "feminino"):
            print("sexo feminino")
        else:
            print("sexo masculino")

    def cep(self, CEP):
        print(CEP)

    def name(self, nome):
        print(nome)


pss1 = Cadastro(nome="Emily", sexo="feminino", idade=19, CEP=13187074)

print(pss1)


        