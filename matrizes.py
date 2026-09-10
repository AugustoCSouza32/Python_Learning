l = int
c = int

l = int(input("Quantas Linha vai ter a matriz: "))
c = int(input("Quantas colunas vai ter a matriz: "))

matriz  = [[0 for x in range(l)] for x in range(c)]

for i in range(0, l):
    for j in range(0, c):
        matriz[i][j] = int(input(f"Elemento [{i},{j}]: "))


print()

for i in range(0, l):
    for i in range(0, c):
        print(matriz[i][j])
        