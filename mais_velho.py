# Fazer um programa para ler um conjunto de nomoes de pessoas e suas respectivas idades.
# Os nomes devem ser armazenados em um vetor, e as idades em outro vetor. Depois,
# mostrar na tela o nome da pessoa mais velha.

n = int(input("Quantas pessoas você vai digitar: "))

nomes = ["x" for _ in range(n)]
idades = [0 for _ in range(n)]

y = 0
for i in range(n):
    y += 1
    print(f"Dados da {y}ª pessoa: ")
    nomes[i] = input("Nome: ")
    idades[i] = int(input("Idades: "))

verifica_idade = idades[0]

for i in range(n):
    if idades[i] > verifica_idade:
        verifica_idade = idades[i]
        maior_idade = i

print(f"Pessoa mais velha: {nomes[maior_idade]}")