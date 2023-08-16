"""
2- Faça um programa que preencha por leitura um vetor de 10 posições, e conta quantos valores diferentes existem no vetor
"""

lista = []
lista2 = []


print("Digite 10 posições: ")
for i in range(10):
    num = int(input(f"Digite o {i + 1}° número: "))
    lista.append(num)
for num in lista:
    if lista.count(num) == 1:
        lista2.append(num)
print(f"Exitem {len(lista2)} números diferentes!")
