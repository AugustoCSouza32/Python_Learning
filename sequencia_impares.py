# Leia um valor inteiro X. Em seguida mostre  os impares de 1 até X,
# um valor por linha, inclusive o X, se for o caso.

x = int(input("Digite o valor de X: "))

for i in range(1, x+1):
    if i % 2 != 0:
        print(i)