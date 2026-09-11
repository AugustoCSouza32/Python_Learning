#No arremesso de dardo, o atleta tem três chances para lançar o dardo à maior distância que conseguir.
#Você deve criar um programa para, dadas as medidas das três tentativas de lançamento, informar qual foi a maior.

print("Digite as distâncias das três tentativas: ")
dist_1 = float(input())
dist_2 = float(input())
dist_3 = float(input())

if dist_1 > dist_2 and dist_1 > dist_3:
    print("Maior distância: ", dist_1)
elif dist_2 > dist_3:
    print("Maior distância: ",dist_2)
else:
    print("Maior distância: ",dist_3)


