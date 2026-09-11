#Fazer um programa para ler uma duração de tempo em segundos, daí imprimir na tela
#esta duração no formato horas:minutos:segundos

duracao_segundos = int(input("Digite a duração em segundos: "))

horas  = duracao_segundos // 3600

resto = duracao_segundos % 3600

minutos = resto // 60

segundos = resto % 60

print(f"{horas} : {minutos} : {segundos}")