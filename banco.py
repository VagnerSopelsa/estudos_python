import os,datetime,time


menu = """
##### Menu #####
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0 
limite = 500
trato = ""
numero_saques = 0
LIMITE_SAQUES = 3
salva_extrato = ""

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def depositar (valor):

    global saldo
    global salva_extrato    

    data_hora_atual = datetime.datetime.now()
    data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M")

    if valor > 0:
        saldo += valor
        salva_extrato += f"Depósito: R${valor:.2f} Data: {data_hora_formatada}\n"
        print("Deposito Realizado!")
        time.sleep(2)
        limpar_console()
    else:
        print("Depósito falhou! Valor informado inválido.")
        time.sleep(2)
        limpar_console()


def sacar(valor):
    global saldo
    global limite
    global salva_extrato
    global numero_saques
    global LIMITE_SAQUES

    data_hora_atual = datetime.datetime.now()
    data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M")

    if valor > saldo:

        print("Operação falhou! Saldo Insuficiente.")
        time.sleep(2)
        limpar_console()

    elif valor > limite:
         
         print("Operação falhou! Valor do saque exedeu o limite da conta.")
         time.sleep(2)
         limpar_console()

    elif numero_saques >= LIMITE_SAQUES:

        print(f"Operação falhou! Numero maximo de {numero_saques} excedido.")
        time.sleep(2)
        limpar_console()

    elif valor > 0:

        saldo -= valor
        salva_extrato += f"   Saque: R${valor:.2f} Data: {data_hora_formatada}\n"
        numero_saques += 1
        print("Saque Realizado! Retire seu valor na boca do caixa")
        time.sleep(2)
        limpar_console()
    else:
        print("Saque falhou! Valor informado inválido.")
        time.sleep(2)
        limpar_console()


def imprimir_extrato():
    global saldo
    global salva_extrato

    cabecalho = "EXTRATO"

    print(cabecalho.center(50, "#"))
    print("Não foram realizadas movimentações." if not salva_extrato else salva_extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print( "".center(50, "#"))
    input("Pressione Enter para continuar...")
    limpar_console()

    


while True:

    opcao = input(menu)
    
    if opcao.lower() == "d":
         
        try:
            valor_deposito = float(input("Informe o valor do depósito: "))
            depositar(valor_deposito)
        except ValueError:
             print("Valor inválido. Por favor, insira um valor numérico válido.")
             time.sleep(1)
             limpar_console()
         
    elif opcao.lower() == "s":
        try:
            valor_saque = float(input("Informe o valor do saque: "))
            sacar(valor_saque)
        except ValueError:
             print("Valor inválido. Por favor, insira um valor numérico válido.")
             time.sleep(1)
             limpar_console()

    elif opcao.lower() == "e":

        imprimir_extrato()

    elif opcao.lower() == "q":
        break
    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")
    