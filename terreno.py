#Fazer um programa para ler as medidas da largura e comprimento de um terreno
#retangular com uma casa decimal, bem como o valor do metro quadrado do terreno com duas casas decimais.
#Em seguida, o programa deve mostrar o valor da área do terreno, bem como o valor do preço do terreno, ambos
#com duas casas decimais.

largura_terreno = float(input("Digite a largura do terreno: "))
comprimento_terreno = float(input("Digite o comprimento do terreno: "))
valor_metro = float(input("Digite o valor do metro quadrado: "))


area_terreno = largura_terreno * comprimento_terreno
preco_terreno = area_terreno * valor_metro

print(f"Área do terreno: {area_terreno:.1f}".format(area_terreno))
print(f"Valor do terreno: R$ {preco_terreno:.2f}".format(preco_terreno))