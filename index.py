menu = """"

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        valor_deposito = float(input("Quantia:"))
        saldo = saldo + valor_deposito
        extrato = str(extrato + f"+R$ {valor_deposito:.2f}\n")

    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saque diario atingido!")
        else:
            print ("Saque")
            valor_saque = float(input("Quantia:"))
            if valor_saque <= saldo and valor_saque < 500:
                saldo = saldo - valor_saque
                print ("Saque realizado!")
                extrato = str(extrato + f"-R$ {valor_saque:.2f}\n")
                numero_saques = numero_saques + 1
            elif valor_saque > saldo:
                print("Saldo indisponivel")
            elif valor_saque > 500:
                print("Limite ultrapassado")

    elif opcao == "e":
        print("Extrato:")
        print(extrato)
        print(f"R$ {saldo:.2f}")
        
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operaçao desejada")
