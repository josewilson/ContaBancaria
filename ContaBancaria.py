class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.depositos = []
        self.saques = []
        self.saques_realizados = 0

    def formatar_valor(self, valor):
        return f"R$ {valor:.2f}"

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito realizado: {self.formatar_valor(valor)}")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if self.saques_realizados < 3 and valor <= 500:
            if valor <= self.saldo:
                self.saldo -= valor
                self.saques.append(valor)
                self.saques_realizados += 1
                print(f"Saque realizado: {self.formatar_valor(valor)}")
            else:
                print("Não foi possível sacar o dinheiro por falta de saldo.")
        else:
            print("Limite de saques diários atingido ou valor de saque inválido.")

    def extrato(self):
        print("\n--- Extrato ---")
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
        else:
            for deposito in self.depositos:
                print(f"Depósito: {self.formatar_valor(deposito)}")
            for saque in self.saques:
                print(f"Saque: {self.formatar_valor(saque)}")
            print(f"Saldo atual: {self.formatar_valor(self.saldo)}")
        print("----------------\n")

def menu():
    conta = ContaBancaria()

    while True:
        print("\n--- Menu ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        opcao = input("Escolha uma opcao:")

        if opcao == '1':
            valor = float(input("Digite o valor do depósito: "))
            conta.depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor do saque: "))
            conta.sacar(valor)
        elif opcao == '3':
            conta.extrato()
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
menu()
