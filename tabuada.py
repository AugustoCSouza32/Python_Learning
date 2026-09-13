# Ler um número inteiro N, daí mostrar na tela a tabuada de N para 1 a 10.

n = int(input("Deseja a tabuada para qual valor? "))

for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")
    