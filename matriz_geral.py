# Ler uma matriz quadrada de ordem N (Máximo de 10),contendo números reais.
# Em seguida, fazer as seguintes ações:
# a) Calcular e imprimir a soma de todos os elementos positivos da matriz.
# b) Fazer a leitura do índice de uma linha da matriz e, daí, imprimir todos
# os elementos da linha.
# c) Fazer a leitura do índice de uma coluna da matriz e, daí, imprimir todos
# os elementos desta coluna.
# d) alterar a matriz elevando ao quadrado todos os números negativos da mesma.
# em seguida imprimir a matriz altera.

n = int(input("Qual a ordem da matriz? "))

while n < 0 or n > 10:
    print("ERRO!")
    n = int(input("Informe novamente. Qual a ordem da matriz? "))

matriz: list[float] = [[0 for col in range(n)]for lin in range(n)]

matriz_alterada: list[float] = [[0 for col in range(n)]for lin in range(n)]

for lin in range(n):
    for col in range(n):
        matriz[lin][col] = float(input(f"Elemento [{lin},{col}]: "))


#somar todos os positivos
#verifica os negativos e eleva ao quadrado salvando na matriz alterada.
soma = 0
for lin in range(n):
    for col in range(n):
        if matriz[lin][col] > 0:
            soma += matriz[lin][col]
            matriz_alterada[lin][col] = matriz[lin][col]
        else:
            matriz_alterada[lin][col] = matriz[lin][col] ** 2

print(f"Soma dos positivos: {soma}")

linha  = int(input("Escolha uma linha: "))
print("Linha escolhida: ", end=" ")
for col in range(n):
    print(matriz[linha][col], end=" ")

print()

coluna = int(input("Escolha uma coluna: "))
print("Coluna escolhida: ", end=" ")
for lin in range(n):
    print(matriz[lin][coluna], end=" ")

print()

print("Diagonal princial: ",end="")
for lin in range(n):
    for col in range(n):
        if lin == col:
            print(matriz[lin][col], end=" ")

print()

print("Matriz alterada: ")
for lin in range(n):
    for col in range(n):
        print(matriz_alterada[lin][col], end=" ")
    print()
