class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f'Depositado: R${valor:.2f}')
        else:
            print("O valor do depósito deve ser positivo.")

    def retirar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f'Retirado: R${valor:.2f}')
        else:
            print("Valor de retirada inválido ou saldo insuficiente.")

    def exibir_saldo(self):
        print(f'Saldo atual: R${self.__saldo:.2f}')

# Exemplo de uso:
minha_conta = ContaBancaria(100)
minha_conta.depositar(50)
minha_conta.retirar(30)
minha_conta.exibir_saldo()
