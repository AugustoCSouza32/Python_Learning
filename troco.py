#Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
#O programa deve ler o preço unitário, quantidade de unidades compradas deste produto, e o valor em
#dinheiro dado pelo cliente (suponha que haja dinheiro suficiente). Seu programa deve mostar o valor
#do troco a ser devolvido ao cliente.

preco_un = float(input("Preço unitário do produto: "))
qtd_produto = int(input("Quantidade comprada: "))

pagamento = float(input("Dinheiro Recebido: "))

troco = pagamento - (preco_un * qtd_produto)

print(f"Troco: R$ {troco:.2f}".format(troco))