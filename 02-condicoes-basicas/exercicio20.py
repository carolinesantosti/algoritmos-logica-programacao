# Desenvolva um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

print("===== VERIFICADOR DE NÚMERO PAR OU ÍMPAR =====\n")
# Solicita ao usuário que insira um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é par ou ímpar usando o operador módulo
if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")
