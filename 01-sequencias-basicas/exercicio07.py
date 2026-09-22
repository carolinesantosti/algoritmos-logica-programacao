# Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a sua terça parte.
# Ex:
# Digite um número: 9.0
# O dobro de 9.0 é 18.0
# A terça parte de 9.0 é 3.0.

num = float(input("Digite um número:"))
dobro = num * 2
terca_parte = num / 3
print(f"O dobro de {num} é {dobro}.")
print(f"A terça parte de {num} é {terca_parte:.2f}.")
