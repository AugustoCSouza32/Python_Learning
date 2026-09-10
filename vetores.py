n: int

n = int(input("Quantos número você vai digitar? "))

vet = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = float(input("Digite um número: "))

print()
print("Números digitados: ")
for i in range(0, n):
    print(vet[i])
