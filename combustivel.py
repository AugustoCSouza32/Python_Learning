#Um posto de combustíveis deseja determinar qual de seus produtos tem
#a preferência de seus clientes. Escreva um algoritmo para ler o tipo
#de combustível abastecido (codificado da seguinte forma:
#1.Álcool, 2.Gasolina, 3.Diesel, 4.Fim). Caso o contrario informe
#que o código é inválido. O programa será encerrado quandoo código
#informado for o número 4, devendo então mostrar a mensagem "Muito Obrigado"
# bem como as quantidades de cada combustivel

alcool = 0
gasolina = 0
diesel = 0

combustivel = int(input("Informe um codigo (1,2,3) ou 4 para parar: "))

while combustivel != 4:
    match combustivel:
        case 1:
            alcool += 1
        case 2:
            gasolina += 1
        case 3:
            diesel += 1
        case 4:
            print("Muito Obrigado")
        case _:
            print("Código inválido")
    combustivel = int(input("Informe um codigo (1,2,3) ou 4 para parar: "))

print("Alcool: ",alcool)
print("Gasolina: ",gasolina)
print("Diesel: ",diesel)