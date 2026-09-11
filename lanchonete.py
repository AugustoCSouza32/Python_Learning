#Uma lanchonete possui vários produtos. Cada produto possui um código e um preço
#Você deve fazer um programa para ler o código e a quantidade comprada de um produto,
#e dai infomar qual o valor a ser pago, com duas casas decimais.

codigo = int(input("Código do produto: "))
qtd_produto = int(input("Quantidade comprada: "))

match codigo:
    case 1:
        total_compra = qtd_produto * 5.00
        print(f"Valor a pagar: R$ {total_compra:.2f}")
    case 2:
        total_compra = qtd_produto * 3.50
        print(f"Valor a pagar: R$ {total_compra:.2f}")
    case 3:
        total_compra = qtd_produto * 4.80
        print(f"Valor a pagar: R$ {total_compra:.2f}")
    case 4:
        total_compra = qtd_produto * 8.90
        print(f"Valor a pagar: R$ {total_compra:.2f}")
    case 5:
        total_compra = qtd_produto * 7.32
        print(f"Valor a pagar: R$ {total_compra:.2f}")
    case _:
        print("Código inválido")