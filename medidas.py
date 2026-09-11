#Fazer um programa para ler três medidas A, B e C. Em seguida, calcular e mostrar:
#A área do quadrado que tem lado A
#A área do triagulo retângulo que tem base A e altura B
#A área do trapézio que tem bases A e B, e altura C

a = float(input("Digite a medida A: "))
b = float(input("Digite a medida B: "))
c = float(input("Digite a medida C: "))

area_quadrado = a**2

area_tri_retangulo = (a * b) / 2

area_trapezio = ((a + b) * c) / 2

print(f"Area do Quadrado: {area_quadrado:.4f}")
print(f"Area do triagulo: {area_tri_retangulo:.4f}")
print(f"Area do trapézio: {area_trapezio:.4f}")