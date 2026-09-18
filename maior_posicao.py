# Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida,
# Mostrar na tela o maior número do vetor. Mostrar também a posição do maior elemento,
# considerando a primeira posição como 0.

n = int(input("Quantos números vai digitar? "))
vet = [0 for _ in range(n)]

for i in range(n):
    vet[i] = int(input("Digite um número: "))

maior_valor = 0

for i in range(len(vet)):
    if vet[i] > maior_valor:
        maior_valor = vet[i]
        posicao= i

print(f"Maior valor: {maior_valor}")
print(f"Posição do maior valor: {posicao}")

