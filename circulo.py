#Fazer um programa para ler o valor "r" do raio de um circulo, e depois mostra o valor da área
#do circulo com três casas decimais. A fórmula da área do círculo é a seguinte: area = pi.r²

import math

r = float(input("Digite o valor do raio do circulo: "))

area = math.pi * pow(r,2)

print(f"Área: {area:.3f}".format(area))