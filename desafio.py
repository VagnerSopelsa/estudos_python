import os,datetime,time,textwrap

def menu():   
    menu = """\n
    ============== Menu ==============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo Usuário
    [lu]\tListar Usuários
    [q]\tSair
    ==> """
    return input(textwrap.dedent(menu))



def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def depositar (saldo, valor, extrato, /):

    data_hora_atual = datetime.datetime.now()
    data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M")

    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\tData: {data_hora_formatada}\n"
        print("\n === Deposito Realizado com sucesso! ===")
        time.sleep(2)
        limpar_console()
    else:
        print("\n@@@Operação falhou! O valor é informado inválido. @@@")
        time.sleep(2)
        limpar_console()
    return saldo, extrato
    
def sacar(*, valor, saldo, extrato, limite, numero_saques, limite_saques):
     
    data_hora_atual = datetime.datetime.now()
    data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M")

    execedeu_saldo = valor > saldo
    execedeu_limite = valor > limite
    execedeu_saques = numero_saques >= limite_saques

    if execedeu_saldo:

        print("\n@@@ Operação falhou! Você não tem saldo Insuficiente. @@@")
        time.sleep(2)
        limpar_console()

    elif execedeu_limite:
         
         print("\n@@@ Operação falhou! Valor do saque exedeu o limite. @@@")
         time.sleep(2)
         limpar_console()

    elif execedeu_saques:

        print("\n@@@ Operação falhou! Numero maximo de saques excedido. @@@")
        time.sleep(2)
        limpar_console()

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\tData: {data_hora_formatada}\n"
        numero_saques += 1
        print("\n=== Saque Realizado com sucesso! ===")
        time.sleep(2)
        limpar_console()
    else:
        print("\n@@@ Operação falhou! Valor informado é inválido. @@@")
        time.sleep(2)
        limpar_console()
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
 
    cabecalho = "EXTRATO"

    print(cabecalho.center(50, "="))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print( "".center(50, "="))
    input("Pressione Enter para continuar...")
    limpar_console()

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        time.sleep(2)
        limpar_console()
        return
    
    nome = input("Informe o nome Completo: ")
    data_nascimento = input("informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})

    print("=== Usuário criado com sucesso! ===")
    time.sleep(2)
    limpar_console()

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        time.sleep(2)
        limpar_console()
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    time.sleep(2)
    limpar_console()

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
        input("Pressione Enter para continuar...")
        limpar_console()

def listar_usuarios(usuarios):
    for usuario in usuarios:
        linha = f"""\
            CPF:\t{usuario['cpf']}
            Nome:\t{usuario['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
        input("Pressione Enter para continuar...")
        limpar_console()
        
        
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0 
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()
        
        if opcao.lower() == "d":
            
            try:
                valor = float(input("Informe o valor do depósito: "))
                saldo, extrato = depositar(saldo, valor, extrato)

            except ValueError:
                print("Valor inválido. Por favor, insira um valor numérico válido.")
                time.sleep(1)
                limpar_console()
            
        elif opcao.lower() == "s":
            try:
                valor = float(input("Informe o valor do saque: "))

                saldo, extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
                    )
            except ValueError:
                print("Valor inválido. Por favor, insira um valor numérico válido.")
                time.sleep(1)
                limpar_console()

        elif opcao.lower() == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao.lower() == "nu":
            criar_usuario(usuarios)
        
        elif opcao.lower() == "nc":
             
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao.lower() == "lc":
            listar_contas(contas)
        
        elif opcao.lower() == "lu":
            listar_usuarios(usuarios)

        elif opcao.lower() == "q":
            break
        else:
            print("Opção inválida, por favor selecione novamente a operação desejada.")

main()