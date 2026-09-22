# Faça um programa que leia um número inteiro e mostre o seu antecessor e seu sucessor.
# Ex:
# Digite um número: 5
# O antecessor de 5 é 4 
# O sucessor de 5 é 6.

num = int(input("Digite um número: \n"))
antecessor = num - 1
sucessor = num + 1
print(f"O antecessor de {num} é {antecessor}.")
print(f"O sucessor de {num} é {sucessor}.")
