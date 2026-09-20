# Tem-se um conjunto de dados contendo a altura e o gênero (M,F) de N pessoas.
# Fazer um programa que calcule e escreva a maior e a menor altura do grupo,
# a média de altura das mulheres, e o número de homens.

n = int(input("Quantas pessoas serão digitadas? "))

altura_homens = [0 for _ in range(n)]
altura_mulheres =[0 for _ in range(n)]

y = 0
m = 0
for i in range(n):
    y += 1
    altura = float(input(f"Altura da {y}ª pessoa: "))
    genero = input(f"Gênero da {y}ª pessoa: ")

    match genero:
        case "f" | "F":
            altura_mulheres[i] = altura
        case "m" | "M":
            altura_homens[i] = altura
            m += 1

soma_altura = 0
count = 0
for x in altura_mulheres:
    if x > 0:
        soma_altura += x
        count += 1
media_altura = soma_altura / count

print(f"Média das alturas das mulheres: {media_altura:.2f}")
print(f"Número de homens: {m}")