# Fazer um programa para ler um vetor de N números inteiros. Em seguida, mostrar
# na tela a média aritimética somente dos números pares lidos, com uma casa decimal.
# Se nenhum número par for digitado, mostrar a mensagem "Nenhum número par".

n = int(input("Quantos elementos vai ter o vetor: "))

vetor = [0 for _ in range(n)]

for i  in range(n):
    vetor[i] = float(input("Digite um número: "))

tem_par = any(x % 2 == 0 for x in vetor)

soma_pares = 0
qtd_pares = 0
if tem_par:
    for x in vetor:
        if x % 2 == 0:
           soma_pares += x
           qtd_pares += 1

if tem_par:
    media_pares = soma_pares / qtd_pares

    print(f"MÈDIA PARES: {media_pares}")
else:
    print("Não tem números pares.")