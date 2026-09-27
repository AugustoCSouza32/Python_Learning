###
# ler dois números M e N (máximo = 10), e depois ler uma matriz MxN de números inteiros.
# Em seguida, mostar na tela somente os números negativos da matriz.
# ###

m = int(input("Qual a quantidade de linhas? "))
n = int(input("Qual a quantidade de colunas? "))

while (m > 10 or m < 0) or (n > 10 or n < 0):
    print("ERRO! digite novamente.")
    m = int(input("Qual a quantidade de linhas? "))
    n = int(input("Qual a quantidade de colunas? "))

matriz: list[int] = [[0 for col in range(n)] for lin in range(m)]

for lin in range(m):
    for col in range(n):
        matriz[lin][col] = int(input(f"Elemento [{lin},{col}]:"))

tem_negativo = False

print("VALORES NEGATIVOS: ")
for lin in range(m):
    for col in range(n):
        if matriz[lin][col] < 0:
            print(matriz[lin][col])
            tem_negativo = True

if not tem_negativo:
    print("Essa matriz não tem números negativos.")