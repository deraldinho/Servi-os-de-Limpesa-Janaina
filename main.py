class calc:
    metragem = 0.00
    valor = 0.0

    def metragem_limpeza(self, metragem):
        try:
            if (metragem <= 30 and metragem < 300):
                self.metragem = (metragem ^ 2)
            elif (metragem <= 300 and metragem < 700):
                self.metragem = (metragem ^ 2)
        except:
            print('!! Não aceitamos casas com metragem menor que 30m² ou maior que 700m?')

    def tipo_limpeza(self):
        pass

    def adicional_limpeza(self):
        pass


class Interface:
    control = ''
    calc = calc()

    def loop(self):
        self.home()
        self.menu(None)

    def home(self):
        print('Bem-vindo ao Programa de Serviços de Limpesa do Janaina Lessa de Paula')
        print('######################################################################################')

    def menu(self, controle):
        print('------ Menu 1 de 3 - Metragem Limpesa ------')
        calc.metragem_limpeza(30)
        print(calc.valor)


if __name__ == '__main__':
    screen = Interface()
    screen.loop()
