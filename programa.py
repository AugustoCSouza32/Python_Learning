#Calculo área de um trapézio


baseMaior: float
baseMenor: float
altura: float
area: float

baseMaior = float(input("Digite o valor da base maior: "))
baseMenor = float(input("Digite o valor da base menor: "))
altura = float(input("Digite o valor da altura: "))


area = ((baseMaior + baseMenor) * altura) / 2

print("A área do trapézio é: ", area)


