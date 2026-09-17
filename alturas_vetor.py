# Fazer um programa para ler nome, idade e altura de N pessoas.
# Depois mostrar na tela a altura média das pessoas, e mostrar também a
# Porcentagem de pessoas com menos de 16 anos, bem como os nomes desas pessoas
# caso houver.

nome: list[str]
idade: list[int]
altura: list[float]

qtd_pessoas: int

qtd_pessoas = int(input("Quantas pessoas serão digitadas: "))
nome = ["-" for _ in range(qtd_pessoas)]
idade = [0 for _ in range(qtd_pessoas)]
altura = [0 for _ in range(qtd_pessoas)]

for i in range(qtd_pessoas):
    print(f"Dados da {i}ª pessoa: ")
    nome[i] = input("Nome: ")
    idade[i] = int(input("Idade: "))
    altura[i] = float(input("Altura: "))


soma_altura = 0
for i in altura:
    soma_altura += altura[i]

altura_media = soma_altura / len(altura)

qtd_idades_menor = 0
for i in idade:
    if idade[i] < 16:
        qtd_idades_menor += 1

porcentagem_menor = (qtd_idades_menor / len(idade)) * 100

print("Altura média: ", altura_media)
print("Pessoas com menos de 16 anos: ", porcentagem_menor)
for i in nome:
    if idade[i] < 16:
        print(nome[i])