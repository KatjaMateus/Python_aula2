nome = "Abel"
idade = 28
altura = 1.79
acidentado = True

lista = ["Ana", "João", "Antonio", "José", "Igor"]

print(lista[1])

print(lista[len(lista) -1])

print(lista[2:4])  #fatia

lista[1] = "Abel"

print(lista)

lista = ["Ana", "João", "Antonio", "José", "Igor", [2,5,7,13], "Otto"]

print(lista[5][2])

lista[-1] = "Teste"
print(lista)
