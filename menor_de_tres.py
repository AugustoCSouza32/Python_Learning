#Fazer um programa para ler três números inteiros. Em seguida,
#mostrar qual é o menor dentre os três números lidos.
#Em caso de empate mostrar apenas uma vez.

primeiro_valor = int(input("Primeiro Valor: "))
segundo_valor = int(input("Segundo Valor: "))
terceiro_valor = int(input("Terceiro valor: "))

if primeiro_valor < segundo_valor and primeiro_valor < terceiro_valor:
    print("Menor: ",primeiro_valor)
elif segundo_valor < terceiro_valor:
    print("Menor: ",segundo_valor)
else:
    print("Menor: ",terceiro_valor)