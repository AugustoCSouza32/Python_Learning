#Fazer um programa para ler a quantidade de glicose no sangue de uma
#pessoa e depois mostrar na tela a classificação desta glicose de acordo
#com a tabela de referência: Normal <= 100mg/dl, Elevado > que 100 e <= 140mg/dl, Diabetes > 140

glicose = float(input("Digite a medida da glicose: "))
classificacao: str

if glicose <= 100:
    classificacao = "NORMAL"
elif glicose > 100 and glicose <= 140:
    classificacao = "ELEVADO"
else:
    classificacao = "DIABETES"

print("Classificação: ",classificacao)