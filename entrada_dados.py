salario1: float
salario2: float
nome1: str
nome2: str
idade: int
sexo: str

nome1 = input("Digite o nome do primeiro funcionário: ")
salario1 = float(input("Digite o salário do primeiro funcionário: "))
nome2 = input("Digite o nome do segundo funcionário: ")
salario2 = float(input("Digite o salário do segundo funcionário: "))
idade = int(input("Digite a idade do funcionário: "))
sexo = input("Digite o sexo do funcionário (M/F): ")


print(f"Nome do primeiro funcionário: {nome1}")
print(f"Salário do primeiro funcionário: {salario1}")
print(f"Nome do segundo funcionário: {nome2}")
print(f"Salário do segundo funcionário: {salario2}")
print(f"Idade do funcionário: {idade}")
print(f"Sexo do funcionário: {sexo}")