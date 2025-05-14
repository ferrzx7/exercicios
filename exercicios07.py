clientes = []

def obter_dados_dos_clientes():
    nome_cliente = input("informe seu nome completo")
    CPF_cliente = int(input("digite seu CPF"))
    RG_cliente = int(input("digite seu RG"))
    nascimento_cliente = float(input("informe sua data de nascimento"))
    endereco_cliente = input("digite seu endereço")
    cidade_cliente = input("informe sua cidade")
    estado_cliente = input("informe seu estado")
    telefone_cliente = (input("informe seu telefone"))
    celular_cliente = int("informe seu celular")
    email_cliente = input("informe seu email")
    
    cliente = {
        "nome_cliente": nome_cliente,
        "CPF_cliente": CPF_cliente,
        "RG_cliente": RG_cliente,
        "Nascimento_cliente":  nascimento_cliente,
        "Endereco_cliente": endereco_cliente,
        "Cidade_cliente": cidade_cliente,
        "Estado_cliente": estado_cliente,
        "telefone_cliente": telefone_cliente,
        "celular_cliente": celular_cliente,
        "email_cliente": email_cliente,

    }

    return clientes

def cadastrar_clientes(dados_clientes):
    clientes.append(dados_clientes)

    return clientes

def mostrar_dados_clientes(dados_clientes):
    for cliente in dados_clientes:
        print(f"""
            nome do cliente : {cliente["nome do cliente"]}")
            CPF do cliente : {cliente["CPF do cliente"]}")
            RG do cliente : {cliente["RG do cliente"]}")
            Data de Nascimento do cliente : {cliente["data de nascimento do cliente"]}")
            endereco do cliente : {cliente["endereco do cliente"]}")
            cidade do cliente : {cliente["cidade do cliente"]}")
            estado do cliente : {cliente["estado do cliente"]}")
            telefone do cliente : {cliente["telefone do cliente"]}")
            celular do cliente : {cliente["celular do cliente"]}")
            email do cliente : {cliente["email do cliente"]}")
""")
        
def iniciar_sistema():
    while True:
        print ("")
        print("="*80)
        print("Opcao 1- Mostrar lista de clientes")
        print("Opcao 2- cadastrar clientes")
        print("Opcao 3- sair do sistema")
        print("="*80)

        opcao = input("escolha uma das opcao do Menu : ")

        if opcao == "1":
            mostrar_dados_clientes(clientes)
        elif opcao == "2":
         cadastrar_clientes(obter_dados_dos_clientes())
        elif opcao == "3":
            print("sistema finalizado")
            break
        else:
            print("opcao invalida, escolha uma das opcao no menu.")

iniciar_sistema()
