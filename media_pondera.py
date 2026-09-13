# Leia um valor inteiro N,que representa o número de casos de teste
# que vem a seguir. Casa caso de teste consiste em 3 valores reais,
# para os quais você deverá calcular e mostrar a média ponderada, sendo
# que o primeiro valor tem peso 2, o segundo tem peso 3 e o teceiro valor
# tem peso 5. Vale lembrar que a média ponderada é a soma de todos os valores
# multiplicados pelo seus respectivos pesos,dividida pela soma dos pesos.


n = int(input("Quantos casos você vai digitar: "))

for i in range(n):
    print("Digite três notas:")
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())

    media_p = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / (2 + 3 + 5)
    print(f"MÉDIA: {media_p:.1f}".format(media_p))