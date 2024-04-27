menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor do deposito: "))
        saldo += valor_deposito
        extrato += f"\nDeposito de R${valor_deposito:.2f}  -  Saldo de R${saldo:.2f}"
        print(f"Deposito de R${valor_deposito:.2f} com sucesso! Saldo de R${saldo:.2f}.")

    elif opcao == "s":

        if numero_saques == 3:
            print("Você atingiu o limites de saques!")

        elif saldo == 0:
            print("Você não possui saldo.")

        else:
            valor_saque = float(input("Digite o valor do saque: "))

            while valor_saque > limite or valor_saque > saldo:

                if valor_saque > limite:
                    resposta = str(input("O valor ultrapassou o limite de R$500.00 por saque. Deseja tentar novamente? (s/n)"))

                elif valor_saque > saldo:
                    resposta = str(input("O valor ultrapassou o seu saldo. Deseja tentar novamente? (s/n)"))

                if resposta == "s":
                    valor_saque = float(input("Digite o valor do saque: "))

                elif resposta == "n":
                    break

                else:
                    print("Resposta inválida, tente novamente.")

            if valor_saque <= limite and valor_saque <= saldo:
                numero_saques += 1
                saldo -= valor_saque
                extrato += f"\nSaque de R${valor_saque:.2f}  -  Saldo de R${saldo:.2f}"
                print(f"Saque de R${valor_saque:.2f} com sucesso! Saldo de R${saldo:.2f}.")

    elif opcao == "e":
        print()
        print("="*50)
        print("Extrato".center(50))
        print("="*50, end="")
        print(extrato, end="\n\n")
        print(f"Saldo: R${saldo:.2f}")
        print("="*50)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")