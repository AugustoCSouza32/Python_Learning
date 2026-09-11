#Uma operadora de telefonia cobra R$ 50.00 por um plano que dá direito a 100 minutos de telefone.
#Cada minuto que exceder a franquia de 100 minutos custa R$ 2.00. Fazer um programa para ler a
#quantidade de minutos que uma pessoa consumiu, daí mostrar o valor a ser pago.

MIN_PLANO = 100
VALOR_PLANO = 50.00
CUSTO_MIN = 2.00
valor_pagar: float
qtd_minutos = int(input("Digite a quantidade de minutos: "))

if qtd_minutos <= MIN_PLANO:
    valor_pagar = VALOR_PLANO
else:
    valor_pagar = ((qtd_minutos - MIN_PLANO) * CUSTO_MIN) + VALOR_PLANO

print(f"Valor a pagar: R$ {valor_pagar:.2f}".format(valor_pagar))