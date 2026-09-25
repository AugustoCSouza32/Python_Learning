###
# Ler um N (máximo = 10) e uma matriz quadrada de ordem N contendo números inteiros.
# Mostrar a soma dos elementos acima da diagonal principal.
# ###

n = int(input("Qual a ordem da matriz? "))
while n < 1 or n > 10:
    print("Erro! Informe novamente.")
    n = int(input("Qual a ordem da matriz? "))

matriz: list[int] = [[0 for col in range(n)]for lin in range(n)]

for lin in range(n):
    for col in range(n):
        matriz[lin][col] = int(input(f"Elemento [{lin},{col}]: "))

soma = 0
col = 0
for lin in range(n-1):
    for col in range(lin + 1, n):
        soma += matriz[lin][col]
    

print(f"Soma dos elementos acima da diagonal principal: {soma}")