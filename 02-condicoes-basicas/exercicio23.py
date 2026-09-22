# Numa promoção esclusiva para o Dia da Mulher, uma loja quer dar descontos para todos, mas especialmente para mulheres.
# Faça um programa que leia nome, sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo que:
# - Homens ganham 5% de desconto
# - Mulheres ganham 13% de desconto

print("----------- PROMOÇÃO EXCLUSIVA ----------")
nome = input("Qual o seu nome: ")
sexo = input("Informe seu sexo [M/F]: ")
valor_compras = float(input("Qual foi o valor das compras: R$ "))

# Calcula o desconto com base no sexo do cliente
if sexo.upper() == 'F':
    desconto = valor_compras * 0.13
    valor_final = valor_compras - desconto
    print(f"{nome}, você recebeu um desconto de 13%. O valor final das suas compras é: R$ {valor_final:.2f}.")
elif sexo.upper() == 'M':
    desconto = valor_compras * 0.05
    valor_final = valor_compras - desconto
    print(f"{nome}, você recebeu um desconto de 5%. O valor final das suas compras é: R$ {valor_final:.2f}.")
else:
    print("Sexo inválido. Por favor, informe 'M' para masculino ou 'F' para feminino.")
