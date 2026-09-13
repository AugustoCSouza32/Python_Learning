# Leia 2 valores inteiros X e Y (em qualquer ordem). A seguir, calcule
# e mostre a soma dos números impares entre eles.

soma = 0

print("Digite dois números: ")
num_1 = int(input())
num_2 = int(input())

if num_1 > num_2:
    troca = num_1
    num_1 = num_2
    num_2 = troca

soma = 0
for i in range(num_1+1, num_2):
    if i % 2 != 0:
        soma += i

print("Soma dos impares: ", soma)