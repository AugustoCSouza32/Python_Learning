# Faça um programa que leia um número inteiro positivo N (máximo = 10)
# e depois X números inteiros e armazene-os em um vetor. Em seguida
# mostrar na tela todos os números negativos lidos.

n = int(input("Quantos números você vai digitar? "))

while n < 0:
    print("Informe um número positivo: ")
    n = int(input("Quantos números você vai digitar? "))

vet = [0 for _ in range(n)]

for i in range(n):
    vet[i] = int(input("Digite um número: "))

tem_negativo = False
for num in vet:
    if num < 0:
        tem_negativo = True
        break

if n == 0:
    print("NULL")
elif tem_negativo == False:
    print("Vetor com apenas positivos")
else:
    print("Números negativos: ")

for i in range(n):
    if vet[i] < 0:
        print(vet[i])
