def sacar(*, saldo, valor_saque, extrato, limite, numero_saques, limite_saques):
    
    if numero_saques == limite_saques:
        print("\nVocê atingiu o limites de saques!")
        return (saldo, extrato, numero_saques)

    elif saldo == 0:
        print("\nVocê não possui saldo.")
        return (saldo, extrato, numero_saques)

    else:
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
            print(f"\nSaque de R${valor_saque:.2f} com sucesso! Saldo de R${saldo:.2f}.")
            return (saldo, extrato, numero_saques)

def deposito(saldo, valor_deposito, extrato, /):
    saldo += valor_deposito
    extrato += f"\nDeposito de R${valor_deposito:.2f}  -  Saldo de R${saldo:.2f}"
    print(f"\nDeposito de R${valor_deposito:.2f} com sucesso! Saldo de R${saldo:.2f}.")
    return (saldo, extrato)

def extratos(saldo, /, *, extrato):
    print()
    print("="*50)
    print("Extrato".center(50))
    print("="*50, end="")
    print(extrato, end="\n\n")
    print(f"Saldo: R${saldo:.2f}")
    print("="*50)

def cadastro_usuario(usuarios, cpf):
    usuario = {}
    nome = str(input("Digite o seu nome: "))
    data_nascimento = str(input("Digite a data de nascimento (dia/mes/ano): "))
    logradouro = str(input("Digite o logradouro: "))
    numero_casa = str(input("Digite o numero da casa: "))
    bairro = str(input("Digite o bairro: "))
    cidade = str(input("Digite a cidade: "))
    sigla_estado = str(input("Digite a sigla do estado: "))
    endereco = f"{logradouro}, {numero_casa} - {bairro} - {cidade}/{sigla_estado}."

    usuario["nome"] = nome
    usuario["data_nascimento"] = data_nascimento
    usuario["cpf"] = cpf
    usuario["endereco"] = endereco

    usuarios.append(usuario)
    print("\nUsuário cadastrado com sucesso: ")

def criar_conta(contas, numero_conta, cpf):
    conta = {}
    conta["numero da conta"] = numero_conta
    conta["agencia"] = "0001"
    conta["cpf"] = cpf
    conta["saldo"] = 0
    conta["limite"] = 500
    conta["numero_saques"] = 0
    conta["LIMITE_SAQUES"] = 3
    conta["extrato"] = ""

    contas.append(conta)
    print("\nConta criada com sucesso: ")
    return numero_conta + 1

def listar_usuario(usuarios, cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print()
            print("="*50)
            for chave, valor in usuario.items():
                print(f"{chave.title()} : {valor.title()}")
            print("="*50)
            return True

def verificar_existencia_usuario(usuarios, cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return True   

def listar_conta(contas, cpf):
    for conta in contas:
        if conta["cpf"] == cpf:
            print()
            print("="*50)
            for chave, valor in conta.items():
                print(f"{chave.title()} : {valor}")
            print("="*50)

def verificar_existencia_conta(contas, cpf):
    for conta in contas:
        if conta["cpf"] == cpf:
            return True  

menu = """
[u] Cadastrar usuario
[c] Criar conta
[a] Acessar conta
[q] Sair

=>"""

menu_funcoes = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

usuarios = []
contas = []
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
numero_conta = 1


while True:

    opcao = input(menu)

    if opcao == "u":
        cpf = str(input("Digite o cpf: "))
        if verificar_existencia_usuario(usuarios, cpf) == True:
            print("\nEsse cpf já está cadastrado! ")
        else:
            cadastro_usuario(usuarios, cpf)
            listar_usuario(usuarios, cpf)

    elif opcao == "c":
        cpf = str(input("Digite o CPF que deseja vincular a conta: "))
        numero_conta = criar_conta(contas, numero_conta, cpf)
        listar_conta(contas, cpf)

    elif opcao == "a":
        cpf = str(input("Digite o cpf para acessar sua conta: "))
        if verificar_existencia_usuario(usuarios, cpf) == True:
            print("\nAcessando seu usuario...")
            listar_usuario(usuarios, cpf)
            if verificar_existencia_conta(contas, cpf) == True:
                print("\nAcessando sua(s) conta(s)...")
                listar_conta(contas, cpf)
                conta_escolhida = int(input("Digite o numero da conta que deseja acessar: "))
                while True:

                    opcao = input(menu_funcoes)

                    if opcao == "d":
                        valor_deposito = float(input("Digite o valor do deposito: "))
                        contas[conta_escolhida-1]["saldo"], contas[conta_escolhida-1]["extrato"] = deposito(contas[conta_escolhida-1]["saldo"], valor_deposito, contas[conta_escolhida-1]["extrato"])

                    elif opcao == "s":
                        valor_saque = float(input("Digite o valor do saque: "))
                        contas[conta_escolhida-1]["saldo"], contas[conta_escolhida-1]["extrato"], contas[conta_escolhida-1]["numero_saques"] = sacar(saldo=contas[conta_escolhida-1]["saldo"], valor_saque=valor_saque, extrato=contas[conta_escolhida-1]["extrato"], limite=contas[conta_escolhida-1]["limite"], numero_saques=contas[conta_escolhida-1]["numero_saques"], limite_saques=contas[conta_escolhida-1]["LIMITE_SAQUES"]) 

                    elif opcao == "e":
                        extratos(contas[conta_escolhida-1]["saldo"], extrato=contas[conta_escolhida-1]["extrato"])

                    elif opcao == "q":
                        break

                    else:
                        print("\nOperação inválida, por favor selecione novamente a operação desejada.")
            else:
                print("\nVocê possui um usuario cadastrado mas não possui nenhuma conta.")
        else:
            print("\nVocê não possui um usuario cadastrado.")
    elif opcao == "q":
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")