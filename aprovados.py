# Fazer um programa para ler um conjunto de N nomes de alunos, bem como as notas
# que eles tiraram no 1° e 2° semestres. Cada uma dessas informações deve ser 
# armazenada em um vetor. Depois, imprimir os nomes dos alunos aprovados,
# considerando aprovados aqueles cuja média das notas seja maior ou igual a 6.0


n = int(input("Quantos alunos serão digitados?"))
nomes = ["x" for _ in range(n)]
notas_1 = [0 for _ in range(n)]
notas_2 = [0 for _ in range(n)]
media_alunos = [0 for _ in range(n)]

y = 0
for i in range(n):
    y += 1
    print(f"Digite o nome, primeira e segunda nota do {y}° aluno:")
    nomes[i] = input("Nome: ")
    notas_1[i] = float(input("Primeiro Semestre: "))
    notas_2[i] = float(input("Segundo Semestre: "))
    media_alunos[i] = (notas_1[i] + notas_2[i]) / 2

j = 0
print("Alunos aprovados: ")
for nota in media_alunos:
    if nota >= 6.0:
        print(nomes[j])

    j += 1
    