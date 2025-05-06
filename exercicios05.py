def cadastrar_aluno(nome, email, serie):
    alunos = []
    aluno = {
        "nome": nome,
        "email": email,
        "serie": serie,
    }
    
    alunos.append(aluno)
    return alunos
print(cadastrar_aluno("xaulin matador de porco"," xaulinmatador@gmail.com", "2 tb"))