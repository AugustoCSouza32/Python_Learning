# Fazer um programa para ler um número inteiro N e depois um vetor de N números reias.
# Em seguida, mostrar na tela a média aritmética de todos elementos com três casas
# casas decimais. Depois mostrar todos os elementos do vetor que estejam abaixo da
# média, com uma casa decimal cada.

n = int(input("Quantos elementos vai ter o vetor? "))
vet = [0 for _ in range(n)]

for i in range(n):
    vet[i] = float(input("Digite um número: "))

soma=0
for i in vet:
    soma += i

media = soma / len(vet)
print(f"Média do vetor: {media:.3f}")
abaixo_media = 0
print("Elementos abaixo da média:")
for i in vet:
    if i < media:
        print(i)

