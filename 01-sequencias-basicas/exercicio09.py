# Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar.
# Considere US$1,00 = R$ 3,45

reais = float(input("Digite quanto dinheiro você tem na carteira (em R$): "))
dolar = reais / 3.45
print(f"Com R${reais:.2f}, você pode comprar US${dolar:.2f}.")
