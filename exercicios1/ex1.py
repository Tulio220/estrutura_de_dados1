"""
Exercício 01 - 10/08/2023
Dada a lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52] faça um programa que:
a) imprima o maior elemento
b) imprima o menor elemento
c) imprima os números pares
d) imprima o número de ocorrências do primeiro elemento da lista
e) imprima a média dos elementos
1) imprima a soma dos elementos de valor negativo
"""

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

maior_elemento = lista[0]  
for elemento in lista:
    if elemento > maior_elemento:
        maior_elemento = elemento
print(f"O maior elemento da lista é: {maior_elemento}")

menor_elemento = lista[0]  
for elemento in lista:
    if elemento < menor_elemento:
        menor_elemento = elemento
print(f"O menor elemento da lista é: {menor_elemento}")

numeros_pares = []
for elemento in lista:
    if elemento % 2 == 0:
        numeros_pares.append(elemento)
print("Números pares da lista:", numeros_pares)

primeiro_elemento = lista[0]
contador = 0
for elemento in lista:
    if elemento == primeiro_elemento:
        contador += 1
print(f"O primeiro elemento ({primeiro_elemento}) aparece {contador} vezes na lista")


soma_elementos = sum(lista)
media = soma_elementos / len(lista)
print(f"A média dos elementos da lista é: {media:.2f}")

soma_negativos = 0
for elemento in lista:
    if elemento < 0:
        soma_negativos += elemento
print(f"A soma dos elementos de valor negativo é: {soma_negativos}")




