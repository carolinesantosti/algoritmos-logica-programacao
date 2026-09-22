# A locadora de carros precisa da sua ajuda para cobrar seus serviços. 
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado pelo usuário, 
# assim como a quantidade de dias pelos quais o carro foi alugado. 
# O programa deve calcular o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,20 por Km rodado. 

# Solicitação de entrada do usuário
km = float(input("Digite a quantidade de Km percorridos: "))
dias = int(input("Digite a quantidade de dias alugados: "))

# Cálculo do preço por Km, preço por dias e preço total
preco_km = km * 0.20
preco_dias = dias * 90
preco_total = preco_km + preco_dias

# Exibição do preço total a pagar
print(f"O preço total a pagar pelo aluguel do carro é: R$ {preco_total:.2f}.")

