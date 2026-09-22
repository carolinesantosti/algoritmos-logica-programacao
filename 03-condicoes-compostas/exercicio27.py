# Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem final, de acordo com a média atingida:
# - Média até 4.9: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

# Solicita que o aluno informe suas notas
nota1 = float(input("Informe sua primeira nota: "))
nota2 = float(input("Informe sua segunda nota: "))

#Cálculo da média das notas informadas
media = (nota1 + nota2) / 2

# Confere as condições para saber se foi Aprovado, Reprovado ou se está em Recuperação
if media < 5:
    print(f"Sua média foi {media} e você está REPROVADO!")
elif 5 <= media < 7:  # Deixa o limite inferior bem claro
    print(f"Sua média foi {media} e você está de RECUPERAÇÃO!")
else:
    print(f"Sua média foi {media} e você está APROVADO!")

