# Leia um valor inteiro N. Este valor será a quantidade de números inteiros
# que serão lidos em seguida. Para cada valor lido, mostre uma mensagem
# dizendo se este valor é PAR ou IMPAR, e também se é POSITIVO ou NEGATIVO.
# No caso do valor ser igual a zero, o programa deve imprimir apenas NULO.

N = int(input("Quantos números você vai digitar: "))

for i in range(N):
    x = int(input("Digite um número inteiro: "))
    if x % 2 == 0 and x != 0:
        print("PAR ",end="")
    elif x % 2 != 0:
        print("IMPAR ",end="")
    

    if x < 0:
        print("NEGATIVO")
    elif x > 0:
        print("POSITIVO")
    elif x == 0:
        print("NULO")