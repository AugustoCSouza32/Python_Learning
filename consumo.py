#Fazer um programa para ler a distância total (em KM) percorrida por um carro, bem como o
#total de combustível gasto por este carro ao percorrer tal distância. Seu programa deve
#mostrar o consumo médio do carro, com três casas decimais.

distancia = int(input("Distância percorrida: "))
consumo = float(input("Combustível gasto: "))

consumo_medio = distancia / consumo

print(f"Consumo Médio: {consumo_medio:.3f}".format(consumo_medio))