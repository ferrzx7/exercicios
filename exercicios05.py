from exercicios04 import somar_notas

def cadastrar_aluno(nome, email, serie, nota01=0, nota02=0, nota03=0):
    alunos = []

    notas = [nota01, nota02, nota03]

    aluno = {
        "nome": nome,
        "email": email,
        "serie": serie,
        "nota": notas,
        "media": somar_notas(notas)
    }

    alunos.append(aluno)
    media = somar_notas(aluno["nota"])
    return alunos
print(cadastrar_aluno ("gustavo", "gus@gmail.com", "2°TB",8, 9, 8))