#Fazer um programa para ler os três coeficientes de uma equação do segundo grau. Usando a fórmula
#Baskara, calcular e mostrar os valores das raízes x1 e x2 da equação com quatro casas decimais.
#Se a equação não possuir raízes reais, mostrar uma mensagem.
import math


a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente C: "))

if a == 0:
    print("O coeficiente 'a' não pode ser zero.")
else:
    delta = pow(b,2) - 4*a*c
    if delta < 0:
        print("A equação não possui raízes reais.")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)

        x2 = (-b - math.sqrt(delta)) / (2*a)

        print(f"Solução: {x1:.4f} e {x2:.4f}".format(x1,x2))