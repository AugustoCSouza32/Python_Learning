###
# Fazer um programa para ler dois números inteiros M e N (máximo = 10). Em seguida,
# ler uma matriz de M linhas e N colunas contendo números reais. Gerar um vetor de modo
# que cada elemento do vetor seja a soma dos elementos da linha correspondente da matriz
# ###

m = int(input("Qual a quantidade de linhas da matriz? "))

n = int(input("Qual a quantidade de colunas da matriz?"))

matriz = [[0 for col in range(n)] for lin in range(m)]

vetor: list[float] = []

y = 0
for i in range(m):
    y += 1
    print(f"Digite os elementos da {y}ª linha:")
    for j in range(n):
        matriz[i][j] = float(input())


for i in range(m):
    soma = 0
    for j in range(n):
        soma += matriz[i][j]

    vetor.append(soma)

print("Vetor Gerado:")
print(vetor)