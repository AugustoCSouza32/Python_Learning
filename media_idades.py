#Faça um programa para ler um número de dados, contendo cada um, a idade de um indivíduo.
#O último dado, que não entrará nos cáculos, contém um valor de idade negativa. Calcular
#e imprimir a idade média deste grupo de indivíduos. Se for entrada um valor negativo na primeira vez,
#mostrar a mensagem "Impossivel calcular".

idades: int
soma_idades: int
contador: int
media_idades: float

soma_idades = 0
contador = 0

print("Digite as idades: ")
idades = int(input())

if idades >= 0:
    while idades >= 0:
            soma_idades += idades
            contador += 1
            idades = int(input())
    media_idades = soma_idades / contador
    print(f"Média idades: {media_idades:.2f}".format(media_idades))
else:
    print("Impossível Calcular")