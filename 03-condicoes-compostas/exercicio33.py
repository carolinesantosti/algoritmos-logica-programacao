# Escreva um programa para aprovar ou não o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% so salário ou então o empréstimo será negado.

# Solicita que o usuário informe os valores solicitados
valor_casa = float(input("Informe o valor da casa: R$"))
salario = float(input("Informe o seu salário: R$"))
anos = int(input("Em quantos anos deseja pagar? "))

print("---------------------------------")

# Converter anos em meses
total_meses = anos * 12

#Calcular a prestação mensal
prestacao = valor_casa / total_meses

# Calcular o limite de 30%
limite = salario * 0.30

if prestacao <= limite:
    print("EMPRÉSTIMO APROVADO!!")
    print("-------------------------------")
else:
    print("EMPRÉSTIMO NEGADO!!")
    print("-------------------------------")

# Mostra os valores da prestação e do limite
print(f"Prestação mensal: R${prestacao:.2f}")
print(f"Limite de 30%: R${limite:.2f}")
print("-----------------------------------")

