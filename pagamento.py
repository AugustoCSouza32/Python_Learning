#Fazer um programa para ler o nome de um(a) funcionário(a), o valor que ele(a) recebe por hora,
#e a quantidade de horas trabalhadas por ele(a). Ao final, mostrar o valor do pagamento do
#funcionário(a) com uma mensagem.

nome = input("Nome: ")
valor_hora = float(input("Valor por hora: "))
hora_trab = int(input("Horas trabalhadas: "))

pagamento = valor_hora * hora_trab

print(f"O pagamento para {nome} deve ser de R$ {pagamento:.2f}".format(pagamento))