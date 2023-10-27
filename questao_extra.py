# Faça um programa que pede para o usuário cadastrar 5 alunos com nome e nota, e no final mostra o nome e nota do aluno que tirou a maior nota

lista []
for i in range(5):
    nome = str(input("Digite seu nome: "))
    nota = float(input("Digite sua nota: "))
    lista.append(nome)
    lista.append(nota)
    if i > nota:
        print(i)

