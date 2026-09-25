###
# Fazer um programa para ler duas matrizes de números inteiros A e B, contendo
# de M linhas e N colunas cada (M e N máximo 10). Depois gerar uma terceira matriz C
# onde cada elemento desta é a soma dos elementos correspondentes das matrizes originais.
# Imprimir na tela a matriz gerada.
# ###


m = int(input("Quantas linhas vai ter cada matriz? "))
while m < 1 or m > 10:
    print("Erro! Informe novamente.")
    m = int(input("Quantas linhas vai ter cada matriz? "))

n = int(input("Quantas colunas vai ter cada matriz? "))
while n < 1 or n > 10:
    print("Erro! Informe novamente.")
    n = int(input("Quantas linhas vai ter cada matriz? "))

matriz_a: list[int] = [[0 for col in range(n)]for lin in range(m)]
matriz_b: list[int] = [[0 for col in range(n)]for lin in range(m)]
matriz_c: list[int] = [[0 for col in range(n)]for lin in range(m)]

print("Digite os valores da matriz A: ")
for lin in range(m):
    for col in range(n):
        matriz_a[lin][col] = int(input(f"Elemento [{lin},{col}]: "))

print("Digite os valores da matriz B: ")
for lin in range(m):
    for col in range(n):
        matriz_b[lin][col] = int(input(f"Elemento [{lin},{col}]: "))

print("Soma das matrizes A e B: ")
for lin in range(m):
    for col in range(n):
        matriz_c[lin][col] = matriz_a[lin][col] + matriz_b[lin][col]

for lin in range(m):
    for col in range(n):
        print(matriz_c[lin][col], end=" ")
    print()