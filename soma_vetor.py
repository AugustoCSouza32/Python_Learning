# Faça um programa que Leia N números reais e armazene-os em um vetor.
# Em seguida: Imprima todos os elementos do vetor.
# Mostrar na tela a soma e a média dos elementos dos vetor.
soma = 0
n = int(input("Quantos números você vai digitar? "))

vet = [0 for _ in range(n)]

for i in range(n):
    vet[i] = int(input("Digite um número: "))

print("Valores: ", end="")
for i in range(n):
    print(f"{vet[i]:.1f}", end=" ")
    soma += vet[i]

print(f"\nSoma: {soma:.2f}")
media = soma / n
print(f"Média: {media:.2f}")