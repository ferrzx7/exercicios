import json
import os


# clientes = []

db_clientes = "db_clientes.json"
def carregar_dados():
    if os.path.exists(db_clientes):
        with open(db_clientes, "r", enconding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []


def obter_dados_dos_clientes():
    nome_cliente = input("informe seu nome completo: ")
    CPF_cliente = int(input("digite seu CPF: "))
    RG_cliente = int(input("digite seu RG: "))
    nascimento_cliente = input("informe sua data de nascimento: ")
    endereco_cliente = input("digite seu endereço: ")
    cidade_cliente = input("informe sua cidade: ")
    estado_cliente = input("informe seu estado: ")
    telefone_cliente = int(input("informe seu telefone: "))
    celular_cliente = int(input("informe seu celular: "))
    email_cliente = input("informe seu email: ")
    
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

    return cliente


def cadastrar_clientes(dados_clientes):
    clientes = carregar_dados()
    clientes.append(dados_clientes)

    with open(db_clientes, "w", encoding="utf-8") as arq_json:
        json.dump(clientes, arq_json, indent=4, ensure_ascii=False)


def mostrar_dados_clientes(dados_clientes):
    for cliente in dados_clientes:
        print(f"""
            nome do cliente : {cliente["nome_cliente"]}")
            CPF do cliente : {cliente["CPF_do_cliente"]}")
            RG do cliente : {cliente["RG_do_cliente"]}")
            Data de Nascimento do cliente : {cliente["data_de_nascimento_do_cliente"]}")
            endereco do cliente : {cliente["endereco_do_cliente"]}")
            cidade do cliente : {cliente["cidade_do_cliente"]}")
            estado do cliente : {cliente["estado_do_cliente"]}")
            telefone do cliente : {cliente["telefone_do_cliente"]}")
            celular do cliente : {cliente["celular_do_cliente"]}")
            email do cliente : {cliente["email_do_cliente"]}")
""")
        
def iniciar_sistema():
    clientes = carregar_dados()
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
