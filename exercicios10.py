import json
import os

filmes = 'cadastro_filmes.json'

def cadastrar_dados():
    if os.path.exists(filmes):
        with open(filmes, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []

def obter_dados():
    nome_filme = input("informe o nome do filme: ")
    classificacao = input("informe a classificacao do filme: ")
    descricao = input("informe a descricao do filme: ")
    categoria = input("informe a categoria do filme: ")

    data_filme = {
        "data_filme": nome_filme, 
        "classificacao": classificacao,
        "descricao": descricao,
        "categoria": categoria
    }

    return data_filme

def cadstrar_filmes(receber_filme):
    db_filmes = cadastrar_dados()
    db_filmes. append(receber_filme)

    with open(filmes, "w", encoding="utf-8") as arq_json:
        json.dump(db_filmes, arq_json, indent=4, ensure_ascii=False)

def mostrar_filmes(filmes):
    if filmes:
        for filme in filmes:
            print(f"""
                  nome do filme{filme["nome_filme"]}
                  classificao do filme{filme["nome_filme"]}
                  descricao do filme{filme["nome_filme"]}
                  categoria do filmeV{filme["nome_filme"]}
                  
                  
                 """)
            
        else:
            print("Nao existe nenhum filme cadastrado.")

def iniciar_sistema():
    db_filmes = cadastrar_dados()

    while True:
        print("")
        print("="*80)
        print("opcao 1 - mostrar lista de filme")
        print("opcao 2 - cadastrar filmes")
        print("sair do sistema")
        print("="*80)
       
        opcao = input("escolha uma das opcao no menu: ")
    
        if opcao == "1":
            mostrar_filmes(db_filmes)
        elif opcao == "3":
            print("sistema finalizado!!!")
            break 
        else:
            print("opcao invalida, escolha uma das opcao do menu.")