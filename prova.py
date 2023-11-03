lista = []
lista_pares = []
lista_impares = []
soma_pares = 0
soma_impares = 0

for numeros in range(10):
    numero = int(input("Digite um número: "))
    lista.append(numero)
for numero in lista:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
        
lista = (lista_pares), (lista_impares)
print(f"Os números digitados são: {lista}")
print(f"Os números pares são: {lista_pares}, e os números ímpares são {lista_impares}.")
print(f"A quantidade de números pares é {(len(lista_pares))}, e a quantidade de número ímpares é {(len(lista_impares))}.")

for numero in lista_pares:
    soma_pares += numero
print(f"A soma dos números pares é {soma_pares}.")

for numero in lista_impares:
    soma_impares += numero
print(f"A soma dos números ímpares é {soma_impares}.")

