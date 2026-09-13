#O programa deve ler um valor inteiro X indefinidas vezes. (O programa irá parar quando o
# valor de X for igual a 0. Para cada X lido, imprima a soma dos 5 pares consecutivos a partir)
# de X, se for par. Se o valor de entrada for 4,por exemplo, a saída deve ser 40, que é o 
# resultado da operação: 4+6+8+10+12, enquanto que se o valor de entrada for 11,por exemplo
# a saída deve ser 80, que é o resultado da operação: 12+14+16+18+20

num  = int(input("Digite um número inteiro ou 0 para sair: "))

while num !=0:
    if num % 2 != 0:
        num += 1

    soma = num
    for i in range(0,4):
        num += 2
        soma += num

    print(f"SOMA: {soma}")
    num = int(input("Digite um número inteiro ou 0 para sair: "))