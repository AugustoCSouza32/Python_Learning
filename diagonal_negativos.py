###
# Fazer um programa para ler um número inteiro N (máximo 10) e uma matriz quadrada
# de ordem N contendo números inteiros. Em seguida,mostrar a diagonal principal
# e a quantidade de valores negativos da matriz.
# ###
from rich import print
import subprocess
import os

n = int(input("Qual a ordem da matriz?"))

while n > 10 or n <= 0:
    n = int(input("ERRO, informe um valor de 1 a dez:"))

matriz = [[0 for col in range(n)] for lin in range(n)]

#Preenche os dados na matriz, verifica se o número é negativo e conta.
count = 0
for i in range(n):
    for j in range(n):
        matriz[i][j] = int(input(f"Elemento [{i}{j}]: "))
        if matriz[i][j] < 0:
            count += 1

# Limpa o terminal utilizando subprocess
subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

#Imprime a matriz com a diagonal em destaque
for i in range(n):
    for j in range(n):
        if i == j:
            print(f"[bold yellow]{matriz[i][j]}[/]", end=" ")
        else:
            print(f"{matriz[i][j]}", end=" ")
    print()
print()

#Imprime os valores da diagonal principal
print("Valores da Diagonal: ")
for i in range(n):
    for j in range(n):
        if i == j:
            print(f"{matriz[i][j]}", end=" ")
print()
#Mostra a quantidade de números negativos
if count > 0:
    print(f"Quantidade de negativos: {count}")
else:
    print("Não contém negativos.")