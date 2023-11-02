# Faça um programa que pede para o usuário cadastrar 5 alunos com nome e nota, e no final mostra o nome e nota do aluno que tirou a maior nota

# lista = []
# for i in range(5):
#     nome = str(input("Digite seu nome: "))
#     nota = float(input("Digite sua nota: "))
#     lista.append(nome)
#     lista.append(nota)
#     if i > nota:
#         print(i)

alunos = []
for i in range(5):
    nome = str(input(f"Digite o nome do aluno {i +1}: "))
    nota = float(input(f"Digite a nota do aluno {i +1}: "))
    alunos.append((nome, nota))

maior = 0
nome_maior = ""
for i in alunos:
    if i[1] > maior:
        maior = i[1]
        nome_maior = i[0]

print(f"A maior nota foi {maior} do aluno {nome_maior}")


