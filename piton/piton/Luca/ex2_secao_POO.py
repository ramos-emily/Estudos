"""
Crie uma classe Robo para controlar o objeto R2D2 com os seguintes métodos:
- Construtor: Recebe como atributo a bateria que varia entre 0 e 100 e cria um atributo de instancia chamado estado
que apresenta se o robô está ligado ou desligado.
- liga_desliga: Quando esse método é chamado o robô passa a ser ligado caso esteja desligado e vice-versa.
- movimento: Recebe como atributo uma string, que representa qual o lado que o robô irá andar e decresce o
atributo bateria em 10 para cada execução desse método.
- controle_energia: Imprime os atributos estado e bateria atualizados do Robo.
Crie uma interface de menu para o Usuário decidir o que irá fazer com o Robo, ou seja,
qual método irá acessar. Faça tratamento de erros com Try/Except/Else/Finally.
Trate também as condições especiais como bateria zerada o que irá acontecer com o seu R2D2?
Dentre outros, fica a cargo de cada programador.
"""


class Robo:

    def __init__(self,bateria):
#Método construtor que irá construir nosso objeto
        self.estado = 'Desligado' #Atributo que define se o robo está
                                  #ligado ou desligado
        self.bateria = bateria #Bateria de 0 a 100%

    def liga_desliga(self): #Método que controla a alternância de
                            #ligar ou desligar o robo
        if self.bateria == 0: #Se a bateria for zero faça:
            print('\nRobo sem bateria, carregue-o\n') #Aviso
            self.estado = 'Desligado' #Desliga o robo
        else:
            #Inversão de estado do Robo e aviso
            if self.estado == 'Desligado':
                self.estado = 'Ligado'
                print('\nRobo ligado\n')
            else:
                self.estado = 'Desligado'
                print('\nRobo desligado\n')

    def movimento(self,lado_andar_robo):
        #Método que controla para qual lado ele irá andar
        if self.bateria == 0:
            print('\nBateria zerada, carregue o R2D2\n') #Aviso
        else:
            if self.estado == 'Desligado': #Condição para ligar o robo
                                           #e permitir o movimento
                print('\nRobo desligado, ligue-o para movimentar\n')
            else:
                self.lado_andar_robo = lado_andar_robo #Atualiza
                                                       #atributo
                self.bateria = self.bateria - 10 #Decrescimento da
                                                 #bateria para cada
                                                 #movimento
                if self.bateria == 0: #Caso a bateria chegue em zero,
                                      #desligue-o
                    self.estado = 'Desligado'

    def controle_energia(self): #Imprime as informações do R2D2
        print(self.estado)
        print(self.bateria)

print('-----------------------MENU-----------------------')

try: #Tente
    bateria = -1 #Inicializa em -1 para permitir a entrada no loop
    while bateria > 100 or bateria < 0: #Loop que se repetirá enquanto
                                        #o valor não for entre 0 e 100
        bateria = int(input('Digite a bateria do Robo: ')) #Entrada de dados
    R2D2 = Robo(bateria) #Criação do objeto

except ValueError: #Exceto ValueError
    print('Opcao Invalida') #Aviso
else: #Se não faça:
    finalizar = '' #Variavel de parada do loop
    while finalizar != 'sair':
        try: #Tratando erro de entrada de dado do usuario errada
            #Menu de opcoes
            opcao = int(input('Digite o numero respectivo ao comando que deseja:\n'
                              '1 - Liga/desliga o Robo\n'
                              '2 - Movimentar o Robo\n'
                              '3 - Controle de energia do Robo\n'
                              '4 - Finalizar o programa\n'
                              'Escolha: '))
        except ValueError:
            print('\nOpcao Invalida\n') #Aviso
        else:
            if opcao == 1:
                R2D2.liga_desliga() #Chama o método
            elif opcao == 2:
                R2D2.movimento(input('\nDigite o lado para o qual o robo ira andar: '))
            elif opcao == 3:
               R2D2.controle_energia()
            elif opcao == 4:
                finalizar = 'sair'
            else:
                print('\nDigite um numero de 1 a 4\n ')

finally:
    print('Programa Finalizado') #Finalização









