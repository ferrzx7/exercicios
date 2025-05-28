def cadastrar_filmes(nome_filme, descricao, classificacao, categorias01, categorias02, categorias03):
    filmes = []
    filme = {
        "nome": nome, 
        "descricao": descricao,
        "classificacao": classificacao,
        "categoria": [categorias01, categorias02, categorias03]
    }

    filmes.append(filme)
    return filmes

print(cadastrar_filmes ("batatunhas", "lugar de machos", 12, "acao", "comedia", "romance"))