#Um empresa vai conceder um aumento percentual de salário aos seus funcionários
#dependendo de quanto cada pessoa ganha. Fazer um programa para ler o salário de uma
#pessoa, daí mostrar qual o novo salário desta pessoa depois do aumento, quanto foi o
#aumento e qual foi a porcentagem de aumento.


salario = float(input("Digite o salário da pessoa: "))

if salario <= 1000.00:
    aumento = salario * (20/100)
    novo_salario = salario + aumento
    porcentagem = "20 %"
elif salario > 1000 and salario <= 3000.00:
    aumento = salario * (15/100)
    novo_salario = salario + aumento
    porcentagem = "15 %"
elif salario > 3000.00 and salario <= 8000.00:
    aumento = salario * (10/100)
    novo_salario = salario + aumento
    porcentagem = "10 %"
else:
    aumento = salario * (5/100)
    novo_salario = salario + aumento
    porcentagem = "5 %"

print(f"Novo salário R$ {novo_salario:.2f}")
print(f"Aumento: R$ {aumento:.2f}")
print("Porcentagem: ", porcentagem)
