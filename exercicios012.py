import json
import os

barbeiro = "agenda_barbeiro.json"

def carregar_dados():
     if os.path.exists(barbeiro):
        with open(barbeiro, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
     else:
         return []
     
def obter_dados():
    
    nome_cliente = input("Digite seu Nome por favor: ")
    servico_cliente = input("Digite o serviço desejado por favor: ")
    data_cliente = input("Digite data de agendamento por favor: ")
    horario_cliente = input("Digite a hora por favor: ")
    observaçao_cliente = input("campo opcional, pode ficar vazio: ")

    data_barbeiro = {
    "nome_cliente": nome_cliente,
    "servico": servico_cliente,
    "data": data_cliente,
    "horario": horario_cliente,
    "observacao": observaçao_cliente
    }

    return data_barbeiro

def agenda_barbeiro(cadstrar_clientes):
    db_barbeiro = carregar_dados()
    db_barbeiro.append(cadstrar_clientes)

    with open(barbeiro, "w", encoding="utf-8") as arq_json:
       json.dump(db_barbeiro, arq_json, indent=4, ensure_ascii=False)

def mostrar_agenda(clientes):
    if clientes:
        for data_barbeiro in clientes:
            print(f"""
                    nome do cliente{data_barbeiro["nome_cliente"]}
                    servico do cliente{data_barbeiro["servico"]}
                    data do cliente{data_barbeiro["data"]}
                    horario do cliente{data_barbeiro["horario"]}
                    observacao do cliente{data_barbeiro["observacao"]}


                    """)
    else:
        print("nenhum agendamento. ")

def iniciar_sistema():
    db_barbeiro = carregar_dados()

    while True:
        print("")
        print("="*80)
        print("opcao 1 - serviços agendado")
        print("opcao 2 - marcar servicos")
        print("opcao 3 - sair do sistema")
        print("="*80)
            
        opcao = input("escolha uma das opcao no menu: ")

        if opcao == "1":
            mostrar_agenda(db_barbeiro)
        elif opcao == "2":
            agenda_barbeiro(obter_dados())
        elif opcao == "3":
            print("sistema finalizado!!!")
            break
        else:
            print("opcao invalida, escolha uma das opcao do menu.")
    
iniciar_sistema()



                
            

