def cadastrar_aluno(nome, email, serie, nota01, nota02, nota03):
    alunos = []
    aluno = {
        "nome": nome,
        "email": email,
        "serie": serie,
        "nota": [nota01, nota02, nota03]
    }
    
    alunos.append(aluno)
    return alunos

print(cadastrar_aluno ("xaulinmatadordeporco", "xaulinmatador@gmail.com", "2° TB", 8, 9, 5))
