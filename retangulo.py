#Fazer um programa para ler as medidas da base e altura de um retângulo.
#Em seguida, mostrar o valor da área, perímetro e diagonal deste retângulo,
#com quatro casas decimais.

import math

base_retangulo = float(input("Informe a base do retângulo: "))
altura_retangulo = float(input("Informe a altura do retângulo: "))

perimetro_retangulo = 2 * (base_retangulo + altura_retangulo) #Multiplicação distributiva.

area_retangulo = base_retangulo * altura_retangulo

diagonal_retangulo = math.sqrt(math.pow(base_retangulo, 2) + math.pow(altura_retangulo, 2))

print(f"Área: {area_retangulo:.4f}".format(area_retangulo))
print(f"Perimetro: {perimetro_retangulo:.4f}".format(perimetro_retangulo))
print(f"Diagonal: {diagonal_retangulo:.4f}".format(diagonal_retangulo))