###]
# declaração
# minha_matriz: [[tipo]] = [[0 for x in range(numero_colunas)]for x in range(numero_linhas)]# ###

linhas = int(input("Quantas linhas? "))

colunas = int(input("Quantas colunas? "))

matriz = [[0 for _ in range(colunas)]for _ in range(linhas)]

for i in range(0,linhas):
    for j in range(0, colunas):
        matriz[i][j] = int(input(f"Elementos [{i},{j}]: "))

print()

print("Matriz Digitada:")

for i in range(0,linhas):
    for j in range(0, colunas):
        print(f"{matriz[i][j]}",end=" ")
    print()