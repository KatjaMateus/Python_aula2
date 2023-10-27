lista = []

while len(lista) < 5:
    nome = str(input("Digite o nome:"))
    lista.append(nome)
print(lista)

posicao = int(input("Digite uma posição da lista: "))
nome2 = str(input("Digite um nome: "))

lista.insert(posicao, nome2)
print(lista)
