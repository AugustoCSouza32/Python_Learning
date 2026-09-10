x: int
soma: int
n: int


n = int(input("Quantos números serão digitados? "))

soma = 0

for i in range(0, n):
    x = int(input("Digite um número: "))
    soma += x

print("Soma = ", soma)
