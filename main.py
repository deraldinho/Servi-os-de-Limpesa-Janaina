class Calcular:
    funcionario = 0
    metragem = 0.0
    tipoLimpeza = 0.0
    valor_adicional = 0.0
    valor_total = 0.0

    def metragem_limpeza(self, metragem):
        try:
            metragem = float(metragem)

        except ValueError:
            print('Isso não é um numero')
            return False
        else:
            if 30.0 <= metragem < 300.0:
                self.metragem = metragem
                self.valor_total += 60 + 0.3 * self.metragem
                self.funcionario = 1
                return self.funcionario
            elif 300.0 <= metragem < 700.0:
                self.metragem = metragem
                self.valor_total += 120.0 + 0.5 * self.metragem
                self.funcionario = 2
                return self.funcionario
            else:
                return False

    def tipo_limpeza(self, tipoLimpeza):
        try:
            tipoLimpeza = str(tipoLimpeza)

        except ValueError:
            print('!!!!!! Opção Invalida !!!!!!!')
            return False
        else:
            if tipoLimpeza == 'B' or tipoLimpeza == 'b':
                self.tipoLimpeza = 1.00
                self.valor_total *= 1.00
                return 'B'
            elif tipoLimpeza == 'C' or tipoLimpeza == 'c':
                self.tipoLimpeza = 1.30
                self.valor_total *= 1.30
                return 'C'
            else:
                return False

    def adicional_limpeza(self, adicional_limpeza):
        try:
            adicional_limpeza = int(adicional_limpeza)
        except ValueError:
            return False
        else:
            if adicional_limpeza == 1:
                self.valor_adicional += 10.00
                self.valor_total += self.valor_adicional
                return 1
            elif adicional_limpeza == 2:
                self.valor_adicional += 12.00
                self.valor_total += self.valor_adicional
                return 2
            elif adicional_limpeza == 3:
                self.valor_adicional += 20.00
                self.valor_total += self.valor_adicional
                return 3
            else:
                print('!!!!!! Opção Invalida !!!!!!!')
                return False


def home():
    print('Bem-vindo ao Programa de Serviços de Limpesa do Janaina Lessa de Paula')
    print('######################################################################################')


class Interface:

    def __init__(self):
        self.control = 0
        self.calc = Calcular()

    def loop(self):
        home()
        self.menu_MetragemLimpeza()
        self.menu_TipoLimpeza()
        self.menu_AdicionalLimpeza()

    def menu_MetragemLimpeza(self):
        print('------------------ Menu 1 de 3 - Metragem Limpeza ------------------')
        while True:
            metragem = input("Entre com a metragem da casa: ")
            if not self.calc.metragem_limpeza(metragem):
                print('!! Não aceitamos casas com metragem menor que 30² ou maior que 700M² !!')
            elif self.calc.metragem_limpeza(metragem) == 1:
                print('Sera Necessario(a) um funcionario(a) para a limpeza')
                break
            elif self.calc.metragem_limpeza(metragem) == 2:
                print('Seram Necessarios(as) um funcionarios(as) para a limpeza')
                break
            else:
                pass
        print('######################################################################################')

    def menu_TipoLimpeza(self):

        print('------------------ Menu 2 de 3 - Tipo de Limpeza ------------------')
        while True:
            tipo_limpeza = input("Entre com tipo de limpeza:  \n"
                                 "B - Básica  - Indicada para sujeiras semanais ou quizenais\n"
                                 "C - Completa (30% a mais) - Indicado para sujeiras antigas e/ou não rotineiras\n")
            if not self.calc.tipo_limpeza(tipo_limpeza):
                print('!!!!!! Opção Invalida !!!!!!!')
            elif self.calc.tipo_limpeza(tipo_limpeza) == 'B':
                print('Você selecionou a limpeza BASICA')
                break
            elif self.calc.tipo_limpeza(tipo_limpeza) == 'C':
                print('Você selecionou a limpeza COMPLETA')
                break
            else:
                pass
        print('######################################################################################')

    def menu_AdicionalLimpeza(self):
        print('------------------ Menu 3 de 3 - Adicional de Limpeza ------------------')
        while True:
            self.control = input("0- Não desejo mais nada (encerrar)\n"
                                 "1- Passar 10 peças de roupas - R$ 10.00\n"
                                 "2- Limpeza de 1 Forno/Micro-ondas - R$ 12,00\n"
                                 "3- Limpeza de 1 Geladeira/Freezer - R$ 20,00\n"
                                 ">>> ")

            if self.control == '':
                print('!!!!!! Opção Invalida !!!!!!!')
            else:
                self.control = int(self.control)
                if self.control == 1:
                    self.calc.adicional_limpeza(1)
                elif self.control == 2:
                    self.calc.adicional_limpeza(2)
                elif self.control == 3:
                    self.calc.adicional_limpeza(3)
                elif self.control == 0:
                    print(
                        f'TOTAL: R$ {self.calc.valor_total:,.2f} (metragem: {self.calc.metragem:,.2f} * Tipo: {self.calc.tipoLimpeza:,.2f} + adicional: {self.calc.valor_adicional:,.2f})')
                    break
                else:
                    print('!!!!!! Opção Invalida !!!!!!!')


if __name__ == '__main__':
    screen = Interface()
    screen.loop()
