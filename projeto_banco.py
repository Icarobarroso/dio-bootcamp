def main():
    todos_depositos = []
    todos_saques = []

    while True:
        option = int(input('Insira a opção desejada: 1---> depósito 2---> saque 3----> saldo 4---> extrato 5---> sair '))

        if option == 1:
            deposito = int(input('Quanto deseja depositar?\n'))
            todos_depositos.append(deposito)

        elif option == 2:
            saque = int(input('Quanto deseja sacar?\n'))
            todos_saques.append(saque)
            print(f'Seu saque foi de {saque}')

        elif option == 3:
            saldo = sum(todos_depositos) - sum(todos_saques)
            print(f'Seu saldo é de {saldo}')

        elif option == 4:
            print(f'Depósitos totais: {sum(todos_depositos)}')
            print(f'Saques totais: {sum(todos_saques)}')
            saldo = sum(todos_depositos) - sum(todos_saques)
            print(f'Seu saldo é de {saldo}')

        elif option == 5:
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == '__main__':
    main()