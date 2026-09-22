# Desenvolva um programa que leia uma distância em emtros e mostre os valos relativos em outras medidas.
# Ex: 
# Digite a distância em metros: 185.72
# A distância de 185.72 metros corresponde a:
# 0.18572 quilômetros
# 1.8572 hectômetros
# 18.572 decâmetros
# 1857.2 decímetros
# 18572.0 centímetros
# 18572 milímetros

distancia_metros = float(input("Digite uma distância em metros: "))
print(distancia_metros, "metros corresponde a:")

distancia_quilometros = distancia_metros / 1000
distancia_hectometros = distancia_metros / 100
distancia_decametros = distancia_metros / 10
distancia_decimetros = distancia_metros * 10
distancia_centimetros = distancia_metros * 100
distancia_milimetros = distancia_metros * 1000

print(f"{distancia_quilometros} quilômetros")
print(f"{distancia_hectometros} hectômetros")
print(f"{distancia_decametros} decâmetros")
print(f"{distancia_decimetros} decímetros")
print(f"{distancia_centimetros} centímetros")
print(f"{distancia_milimetros} milímetros")
