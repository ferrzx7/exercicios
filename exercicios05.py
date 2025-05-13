from exercicios04 import somar_notas

alunos = []

def obter_dados_aluno():
    nome_aluno = input("Informe o Nome Completo do Aluno: ")
    email_aluno = input("Informe o Email Completo do Aluno: ")
    serie_aluno = input("Informe a Serie Completo do Aluno: ")
    nota01 = int(input("digite a nota01 do aluno: "))
    nota02 = int(input("digite a nota02 do aluno: "))
    nota03 = int(input("digite a nota03 do aluno: "))

    return cadastrar_aluno(nome_aluno, email_aluno, serie_aluno, nota01, nota02, nota03)

def cadastrar_aluno(nome, email, serie, nota01=0, nota02=0, nota03=0):

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

obter_dados_aluno()

def mostrar_dados_alunos(dados_alunos):
    for aluno in dados_alunos:
            print(f"Nome do Aluno: {aluno["nome"]}")

    return print(dados_alunos)

mostrar_dados_alunos(alunos)
