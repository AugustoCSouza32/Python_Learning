print("Olá, mundo!")
print("Boa noite, mundo!")

#para não pular linha, podemos usar o end="" no final do print
print("Olá, mundo!", end="")
print("Boa noite, mundo!")

nome: str
idade: int

nome = "Augusto"
idade = 32

print("%s tem %d anos" % (nome, idade))

x: float
x = 2.3678

print("O valor de x é {:.2f}".format(x))

#interpolação de strings
idade: int
salario: float
nome: str
sexo: str

idade = 20
salario = 5870.70
nome = "Maria Silva"
sexo = "F"

#usando placeholders
print("A funcionária {:s} do sexo {:s}, ganha R$ {:.2f} e tem {:d} anos".format(nome, sexo, salario, idade))

print("A funcionária %s do sexo %s tem %d anos e recebe R$ %.2f" % (nome, sexo, idade, salario))
#usando f-strings
print(f"A funcionária {nome} do sexo {sexo} tem {idade} anos e recebe R$ {salario:.2f}")
