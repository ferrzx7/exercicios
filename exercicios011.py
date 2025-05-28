import json
import os

veiculo = "cadastro_veiculo.json"

def carregar_dados():
    if os.path.exists(veiculo):
        with open(veiculo, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []
   
def obter_dados():
    modelo_veiculo = input("informe o modelo do veiculo: ")
    marca_veiculo = input("informe a marca do veiculo: ")
    placa_veiculo = input("informe a placa do veiculo: ")
    ano_veiculo = int(input("informe o ano do veiculo: "))
    cor_veiculo = input("informe a cor do veiculo: ")

    data_veiculo = {
    "data_veiculo": modelo_veiculo,
    "marca": marca_veiculo,
    "placa": placa_veiculo,
    "ano": ano_veiculo,
    "cor": cor_veiculo
}
    
    return data_veiculo

def cadastrar_veiculo(receber_veiculo):
    db_veiculo = carregar_dados()
    db_veiculo.append(receber_veiculo)

    with open(veiculo, "w", encoding="utf-8") as arq_json:
        json.dump(db_veiculo, arq_json, indent=4, ensure_ascii=False)

def mostrar_veiculos(veiculos):  
    if veiculos:  
        for veiculo in veiculos:
            print(f"""
                  nome do veiculo{veiculo["data_veiculo"]}
                  marca do veiculo{veiculo["marca"]}
                  placa do veiculo{veiculo["placa"]}
                  ano do veiculo{veiculo["ano"]}
                  cor do veiculo{veiculo["cor"]}
                  
                  
                 """)  
    else:
       print("Nenhum veículo cadastrado no momento.")

def iniciar_sistema():
    db_veiculo = carregar_dados()

    while True:
        print("")
        print("="*80)
        print("opcao 1 - mostrar lista de veiculos")
        print("opcao 2 - cadastrar veiculos")
        print("opcao 3 - sair do sistema")
        print("="*80)
      
        opcao = input("escolha uma das opcao no menu: ")
    
        if opcao == "1":
            mostrar_veiculos(db_veiculo)
        elif opcao == "2":
            cadastrar_veiculo(obter_dados())
        elif opcao == "3":
            print("sistema finalizado!!!")
            break
        else:
            print("opcao invalida, escolha uma das opcao do menu.")
    
iniciar_sistema()