# Faça um programa que leia N números inteiros e armazene-os em um vetor.
# Em seguida, mostre na tela todos os números pares, e também a quantidade de
# números pares.

n = int(input("Quantos número você vai digitar?"))

vet: list[int] = [0 for _ in range(n)]

for i in range(n):
    vet[i] = int(input("Digite um número inteiro: "))

pares = 0
tem_pares: bool = any(x % 2 == 0 for x in vet)

print("Números pares:")
if tem_pares:
    for i in vet:
        if i % 2 == 0:
            print(i, end=" ")
            pares += 1
else:
    print("Não contém números pares.")

print("\nQuantidade de pares: ",pares)