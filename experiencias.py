# Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de
# sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável.
# Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o
# percentual de cada tipo de cobaia utilizada. Este laboratório em especial utiliza três
# tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente
# o número de experimentos que foram realizadas, o tipo de cobaia utilizada e a quantidade
# de cobaias utilizadas em cada experimento. Faça um programa que leia um valor inteiro N
# que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro
# que representa a quantidade de cobais utilizadas e uma letra C, R ou S, indicando o tipo
# de cobaia. Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada
# e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual
# deve ser apresentado com dois digitos após o ponto.

coelhos = 0
ratos = 0
sapos = 0

qtd_casos_testes = int(input("Quantos casos de teste serão digitados: "))

for i in range(qtd_casos_testes):
    qtd_cobaia = int(input("Quantidade de cobaias: "))
    tipo_cobaia = input("Tipo de cobaia (C, R ou S): ")

    match tipo_cobaia:
        case "c" | "C":
            coelhos += qtd_cobaia
        case "r" | "R":
            ratos += qtd_cobaia
        case "s" | "R":
            sapos += qtd_cobaia

print("RELATÓRIO FINAL: ")
total_cobaias = coelhos + ratos + sapos
print(f"Total de cobaias: {total_cobaias}")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")

porcentagem_coelhos = (coelhos / total_cobaias) * 100
porcentagem_ratos = (ratos / total_cobaias) * 100
porcentagem_sapos = (sapos / total_cobaias) * 100

print(f"Percentual de coelhos: {porcentagem_coelhos:.2f} %")
print(f"Percentual de ratos: {porcentagem_ratos:.2f} %")
print(f"Percentual de sapos: {porcentagem_sapos:.2f} %")