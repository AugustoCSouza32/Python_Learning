###
# Leia um inteiro N e uma matriz quadrada de ordem N (máximo 10). Mostrar
# qual o maior elemento de cada linha. Suponha não haver empates.
# ###

n = int(input("Qual a ordem da matriz? "))

matriz: list[int] = [[0 for col in range(n)]for lin in range(n)]

while n <= 0 or n > 10:
    print("ERRO!")
    n = int(input("Informe novamente. Qual a ordem da matriz? "))

for lin in range(n):
    for col in range(n):
        matriz[lin][col] = int(input(f"Elemento [{lin},{col}]: "))

print("Maior elemendo de cada Linha: ")
for lin in range(n):
    maior = matriz[lin][0]
    for col in range(n):
        if matriz[lin][col] > maior:
            maior = matriz[lin][col]

    print(maior)