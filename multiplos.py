#Fazer um programa para ler dois números inteiros, e dizer se um número é múltiplo do outro.
#Os números podem ser digitados em qualquer ordem.

print("Digite dois números inteiros: ")
num_1 = int(input())
num_2 = int(input())

if num_1 > num_2:
    if num_1 % num_2 == 0:
        print("São múltiplos")
    else:
        print("Não são mútiplos")
else:
    if num_2 % num_1 == 0:
        print("São múltiplos")
    else:
        print("Não são múltiplos")