#Escreva um programa que repita a leitura de uma senha até que seja válida.
#Para cada leitura de senha incorreta informada, escrever a mensagem "Senha Invalida! Tente Novamente".
#Quando a senha for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo
#encerrado. Considere que a senha correta seja 2002.

SENHA = 2002

entrada = int(input("Digite a senha: "))

while entrada != SENHA:
    entrada = int(input("Senha invalida! Tente novamente: "))

print("Acesso permitido!")