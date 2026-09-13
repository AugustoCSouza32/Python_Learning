# Fazer um programa para ler um número N, e depois calcular e mostrar o
# fatorial de N.

import sys

# Aumenta o limite para aceitar números maiores em print()


sys.set_int_max_str_digits(300000)


n = int(input("Digite o valor de N: "))

j = n

if n == 0:
    f = 1
else:
    for i in range(1, n):
        f = j * (n-i)
        j = f

print("FATORIAL: ",f)
