#Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
#O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
#e o valor em dinheiro dado pelo cliente. Seu programa deve mostrar o valor do troco a ser devolvido
#ao cliente. Se o dinheiro dado pelo cliente não for suficiente, 
# mostrar uma mensagem informando o valor restante.

preco_un = float(input("Preço unitário do produto: R$ "))
qtd_produto = int(input("Quantidade comprada: "))

total_compra = preco_un * qtd_produto

print(f"Total da compra: {total_compra:.2f}")

dinheiro_receb = float(input("Dinheiro Recebido: R$ "))

if dinheiro_receb < total_compra:
    restante_receb = total_compra - dinheiro_receb
    print(f"Restam: R$ {restante_receb:.2f} para pagar")
elif dinheiro_receb == total_compra:
    print("Obrigado! Volte sempre.")
else:
    troco = dinheiro_receb - total_compra
    print(f"Seu troco: R$ {troco:.2f}")
    print("Obrigado! Volte Sempre.")

