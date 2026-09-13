# Escreva um algoritmo que leia dois números e imprima o resultado
# da divisão do primeiro pelo segundo. Caso não for possivel, mostre
# a mensagem, "DIVISÃO IMPOSSIVEL"

n = int(input("Quantos casos você vai digitar? "))

for i in range(n):
    numerador = float(input("Entre com o numerador: "))
    denominador = float(input("Entre com o denominador: "))

    if denominador == 0:
        print("DIVISÃO IMPOSSIVEL")
    else:
        divisao = numerador / denominador
        print(f"DIVISÃO: {divisao:.2f}".format(divisao))