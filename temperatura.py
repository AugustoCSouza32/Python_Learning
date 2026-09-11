#Deseja-se converter uma medida de temperatura da escala Celsius para Fahrenheit ou vice-versa.
#Para isso, você deve construir um programa que leia a letra "C" ou "F" indicando em qual escala
#vai ser informada uma temperatura. Em seguida o programa deve mostrar a temperatura na outra
#escala com duas casas decimais. A seguir é dada a fórmula para converter de Fahrenheit para Celsius.
# C = (5/9)*(F-32)
# F = (C * 3/5) + 32

print("Qual escala de temperatura você vai informar (C/F)? ")
escala = input()

match escala:
    case "C" | "c":
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = (celsius * (9/5)) + 32
        print(f"Conversão para Fahrenheit: {fahrenheit:.2f}°F".format(fahrenheit))
    case "F" | "f":
        fahrenheit = float(input("Digite a temperatura em Fahreinheit: "))
        celsius = (fahrenheit - 32) / (9/5)
        print(f"Conversão para Celsius: {celsius:.2f}°C")
