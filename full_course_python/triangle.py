
lado_a = int(input("Informe o lado do triângulo: "))

lado_b = int(input("Informe o segundo lado do triângulo: "))

lado_c = int(input("Informe o terceiro lado do triângulo: "))

if lado_a == lado_b and lado_a == lado_c:
    print("Caso 1")
elif lado_a == lado_b or lado_b == lado_c or lado_c == lado_a:
    print("Caso 2")
else:
    print("Caso 3")