"""
3- Faça um programa que preencha por leitura um vetor de 5 posições, e informe a posição em que um valor x (lido do teclado) aparece pela primeira vez no vetor. Caso o valor x não seja encontrado, o programa deve imprimir o valor -1

"""

vetor = []
for _ in range(5):
    value = int(input("Digite um valor: "))
    vetor.append(value)

x = int(input("Digite o valor a ser buscado: "))

position = -1  
for i in range(len(vetor)):
    if vetor[i] == x:
        position = i
        break 

if position != -1:
    print(f"O valor {x} foi encontrado na posição {position}.")
else:
    print(f"O valor {x} não foi encontrado no vetor.")
