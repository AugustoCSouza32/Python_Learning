# Faça um programa para ler dois vetores A e B, contendo N elementos cada.
# Em seguida, gere um terceiro vetor C onde cada elemento de C é a soma dos
# Elementos correspondentes de A e B. Imprima o vetor C gerado.

n = int(input("Quantos valores vai ter cada vetor: "))

a: list[int] = [0 for _ in range(n)]
b: list[int] = [0 for _ in range(n)]
c: list[int] = [0 for _ in range(n)]
for i in range(n):
    a[i] = int(input("A: "))
    b[i] = int(input("B: "))

for i in range(n):
    c[i] = a[i] + b[i]

print("Vetor resultante: ")
for i in c:
    print(i)