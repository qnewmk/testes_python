class Conta:
    def __init__ (self, saldo, clientes, numero):
        self.saldo = saldo
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []

    def resumo(self):
        print('cc numero: {}, saldo {}'
            .format(self.numero,self.saldo))

    def saque (self, valor):
            if valor <= self.saldo:
                self.saldo -= valor   
                self.dep = ('saque')
                self.operacoes.append(('saque',valor))
            else:
                print('saldo insulficiente...')

    def deposito(self, valor):
        self.saldo += valor
        self.dep = ('deposito')
        self.operacoes.append(('deposito',valor))

    def extrato(self):
        #self.operacoes.append('operação: {} valor: {}'.format(self.valor))
        print(self.operacoes)
