# Escreva um algoritmo que leia dois números inteiros e compareos, mostrando na tela uma das mensagens abaixo: 
# - O primeiro valor é maior.
# - O segundo valor é o maior.
# -Não existe valor maior, os dois são iguais.

# O usuário digita dois valores
num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))

# Checa pra saber se os valores digitados são maiores ou não dependendo da sua condição
if num1 > num2:
    print("O primeiro valor é maior!")
elif num2 > num1:
    print("O segundo valor é maior!")
else:
    print("Não existe valor maior, os dois são iguais.")
