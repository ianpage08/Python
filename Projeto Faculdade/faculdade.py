class ContaBancaria:
    def __init__(self, nome, sobrenome, cpf):
        # Atributos privados da conta
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf
        self._saldo = 0.0

    # Método para exibir o saldo atual
    def consultar_saldo(self):
        print(f"Saldo atual: R$ {self._saldo:.2f}")

    # Método para realizar depósito
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido!")

    # Método para realizar saque
    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido!")

    # Método para exibir informações da conta
    def exibir_dados(self):
        print("\nDados do usuário:")
        print(f"Nome: {self._nome} {self._sobrenome}")
        print(f"CPF: {self._cpf}")


def main():
    print("Bem-vindo ao Gerenciamento Bancário!")
    nome = input("Informe seu nome: ")
    sobrenome = input("Informe seu sobrenome: ")
    cpf = input("Informe seu CPF: ")

    # Criação do objeto ContaBancaria
    conta = ContaBancaria(nome, sobrenome, cpf)
    conta.exibir_dados()

    while True:
        # Menu de opções
        print("\nEscolha uma opção:")
        print("1 - Consultar saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Encerrar")
        opcao = input("Opção: ")

        if opcao == "1":
            conta.consultar_saldo()
        elif opcao == "2":
            valor = float(input("Informe o valor para depósito: R$ "))
            conta.depositar(valor)
        elif opcao == "3":
            valor = float(input("Informe o valor para saque: R$ "))
            conta.sacar(valor)
        elif opcao == "4":
            print("Encerrando a aplicação...")
            break
        else:
            print("Opção inválida! Tente novamente.")

    print("Obrigado por usar o sistema bancário!")

if __name__ == "__main__":
    main()
