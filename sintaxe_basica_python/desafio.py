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
        valor = float(input("Informe o valor a ser depositado: "))

        if valor < 0:
            print("O valor informado não pode ser depositado")
        else:
            saldo += valor
            extrato += "Depósito de R$ " + str(valor) + "\n"
            print(
                f"Saldo em conta R$ {saldo:.2f} e depósito de R$ {valor:.2f}")

    elif opcao == "s":
        saque = float(input("Informe o valor do saque: "))

        if saque < 0:
            print("O valor informado é inválido")
        else:

            if saque > saldo:
                print("Saldo insuficiente")
            else:
                if numero_saques < LIMITE_SAQUES:
                    if saque <= limite:
                        saldo -= saque
                        numero_saques += 1
                        extrato += str(numero_saques) + \
                            " saque de R$ " + str(saque) + "\n"
                        print(
                            f"Saldo em conta R$ {saldo:.2f}, saque de R$ {saque:.2f}")
                    else:
                        print(f"O limite por saque é de R$ {limite:.2f}")
                else:
                    print("Você já atingiu o quantidade máxima de saque diário")

    elif opcao == "e":
        print("===============Extrato===============")
        if extrato != "":
            print(extrato)
        else:
            print("Nenhuma movimentação realizada")
        print(f"Saldo: {saldo:.2f}")
        print("=====================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
