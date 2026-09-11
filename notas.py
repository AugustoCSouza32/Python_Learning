#Fazer um programa para ler as duas notas que um aluno obteve no primeiro e segundo trimestre
#de uma disciplina anual. Em seguida, mostrar a nota final que o aluno obteve (com uma casa decimal)
#no ano juntamente com um texto explicativo. Caso a note final do aluno seja inferior a 60,00, mostrar
# a mensagem "REPROVADO".

nota_semestre1 = float(input("Digite a nota do primeiro Semestre: "))
nota_semestre2 = float(input("Digite a nota do segundo Semestre: "))

nota_anual = nota_semestre1 + nota_semestre2

print(f"NOTA FINAL: {nota_anual:.1f}".format(nota_anual))

if nota_anual < 60:
    print("REPROVADO")
else:
    print("APROVADO")