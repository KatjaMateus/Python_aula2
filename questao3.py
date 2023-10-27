produtos = [("Maçã", 2.50), ("Banana", 1.75), ("Laranja", 3.00)]

# calculador = 0
# for i in produtos:
#     print(i[1])
#     calculador += i[1]
# print(calculador)

soma = 0

for produto in produtos:
    soma += produto[1]
print(soma)