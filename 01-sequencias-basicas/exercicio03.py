# Crie um programa que leia o nome e o salário de um funcionário, mostrando no final uma mensagem.
# Ex:
# Nome do funcionário: João da Silva
# Salário: 2000.00
# O funcionário João da Silva tem um salário de R$ 2000.00 em Agosto.

nome = input("Nome do funcionário: \n")
salario = float(input("Salário: \n"))
print(f"O(A) funcionário(a) {nome} tem um salário de R${salario:2.2f} em Agosto.")