# Faça um algoritmo que pergunte a distância que um passageiro deseja percorrer em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

print("*--------------- PASSAGEM DE ÔNIBUS -----------------*")
# Solicite que o usuário informe quantos Km irá percorrer
distancia = float(input("Qual a distância deseja percorrer? [Km] "))

# Verifica a distancia percorrida para aplicar o valor da passagem
if distancia <= 200:
    preco = distancia * 0.5
    print(f"O preço da passagem é de R${preco:.2f}")
else:
    preco = distancia * 0.45
    print(f"O preço da passagem é de R${preco:.2f}")
