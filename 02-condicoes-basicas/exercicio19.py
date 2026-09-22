# Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua média e mostre na tela.
# No final, analise a média e mostre se o aluno teve ou não um bom aproveitamento (se a média for maior ou igual a 7.0).

print("===== CALCULADORA DE MÉDIA ESCOLAR =====\n")

# Solicita ao usuário o nome do aluno
nome_aluno = input("Digite o nome do aluno: ")

# Solicita ao usuário as duas notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
print("-----------------------------------------")

# Calcula a média das notas
media = (nota1 + nota2) / 2

# Mostra a média do aluno
print(f"Sua média é {media:.2f}.")

# Verifica se o aluno teve um bom aproveitamento ou não
if media >= 7.0:
    print(f"{nome_aluno}, sua média é {media:.2f}. Parabéns, você teve um bom aproveitamento!")
else:
    print(f"{nome_aluno}, sua média é {media:.2f}. Infelizmente, você não teve um bom aproveitamento.")