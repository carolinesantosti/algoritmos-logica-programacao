# Crie um programa que leia o número de dias trabalhados em um mês e mostre o salário de um funcionário, 
# sabendo que ele trabalha 8 horas por dia e recebe R$ 25,00 por hora trabalhada.

# Solicitação de entrada do usuário
dias_trabalhados = int(input("Digite o número de dias trabalhados no mês: "))

# Cálculo das horas trabalhadas e do salário
horas_trabalhadas = dias_trabalhados * 8
salario = horas_trabalhadas * 25

# Exibição do salário
print(f"O salário do funcionário é: R$ {salario:.2f}.")