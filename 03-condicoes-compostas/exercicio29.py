# Desenvolva um programa que leia o nome de um funcionário, seu salário, quantos anos ele trabalha na empresa 
# e mostre seu novo salário, reajustado de acordo com a tabela a seguir:
# - Até 3 anos de empresa: aumento de 3%
# - Entre 3 e 10 anos: aumento de 12.5%
# - 10 anos ou mais: aumento de 20%

print("\n========== CÁLCULO NOVO SALÁRIO ===========")

# Solicita os dados ao funcionário
nome = input("Informe seu nome: ")
salario_atual = float(input("Informe seu salário: "))
anos = int(input("Quantos anos você trabalha na empresa? "))

# Verifica o tipo de aumento de acordo com a tabela
if anos <= 3:
    salario_novo = salario_atual * 1.03
    print(f"{nome}, seu novo salário com 3% de aumento é de R${salario_novo:.2f}")
elif anos <= 10:
    salario_novo = salario_atual * 1.125
    print(f"{nome}, seu novo salário com 12.5% de aumento é de R${salario_novo:.2f}")
else:
    salario_novo = salario_atual * 1.20
    print(f"{nome}, seu novo salário com 20% de aumento é de R${salario_novo:.2f}")