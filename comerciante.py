###
# Um comerciante deseja fazer o levantamento do lucro das mercadorias que ele
# comercializa. Para isto, mandou digitar um conjunto de N mercadorias, cada
# uma contendo nome, preço de compra e preço de venda das mesmas. Fazer um 
# programa que leia tais dados e determine quatas mercadorias proporcionam:
# Lucro < 10%
# 10% <= lucro <= 20%
# lucro > 20%
# Determine e escreva também o valor de compra e de venda de todas as mercadorias
# assim como o lucro total.
# ###
import os
import subprocess

n = int(input("Quantos produtos serão digitados? "))
nomes = [0 for _ in range(n)]
preco_compra = [0 for _ in range(n)]
preco_venda = [0 for _ in range(n)]

y = 0

for i in range(n):
    y += 1
    print(f"Produto {y}: ")
    nomes[i] = input("Nome: ")
    preco_compra[i] = float(input("Preço de compra: "))
    preco_venda[i] = float(input("Preço de venda: "))

subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

print("Relatório: ")

j = 0
count_10 = 0
count_20 = 0
count_acima = 0
compra_total = 0
venda_total = 0
lucro_total = 0
menor_10 = []
entre_20 = []
maior_20 = []
while j < n:
    lucro = preco_venda[j] - preco_compra[j]
    margem = (lucro / preco_venda[j]) * 100
    if margem < 10:
        count_10 += 1
        menor_10.append(nomes[j])
    elif margem >= 10 and margem <= 20:
        count_20 += 1
        entre_20.append(nomes[j])
    elif margem > 20:
        count_acima += 1
        maior_20.append(nomes[j])

    lucro_total += lucro
    venda_total += preco_venda[j]    
    compra_total += preco_compra[j]
    j += 1

print("-"*20)
print(f"Lucro abaixo de 10%: {count_10}")
for nomes in menor_10:
    print(nomes)
print("-"*20)
print(f"Lucro entre 10% e 20%: {count_20}")
for nomes in entre_20:
    print(nomes)
print("-"*20)
print(f"Lucro acima de 20%: {count_acima}")
for nomes in maior_20:
    print(nomes)
print("-"*20)
print(f"Valor total de compra: R${compra_total:.2f}")
print(f"Valor total de venda: {venda_total:.2f}")
print(f"Lucro total: {lucro_total:.2f}")
print("-"*20)