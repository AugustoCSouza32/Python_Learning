# Fazer um programa para ler um número N {n >= 0 e n <=15}, e depois calcular e mostrar o
# fatorial de N.

import sys

# Aumenta o limite para aceitar números maiores em print()


sys.set_int_max_str_digits(300000)



n = int(input("Digite o valor de N: "))

while n > 15 or n < 0:
    print("Erro informe um número de 0 a 15")
    n = int(input("Digite o valor de N: "))



j = n
if n == 0:
    f = 1
else:
    for i in range(1, n):
        f = j * (n-i)
        j = f

print("FATORIAL: ",f)
