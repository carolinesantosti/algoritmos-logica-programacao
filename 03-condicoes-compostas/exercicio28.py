# Faça um programa que leia a largura e o comprimento de um terreno retangular, calculando e mostrando a sua área em m².
# O programa também deve mostrar a classificação desse terreno, de acordo com a lista abaixo:
# - Abaixo de 100m² = TERRENO POPULAR
# - Entre 100m² e 500m² = TERRENO MASTER
# - Acima de 500m² = TERRENO VIP

# Solicita o usuário que informe a largura e comprimento do terreno
largura = float(input("Informe a largura do terreno: "))
comprimento = float(input("Informe o comprimento do terreno: "))

#Cálculo para saber a área total do terreno
area = largura * comprimento

# Verifica seo terreno de acordo com o tamanho da sua área é Popular, Master ou VIP
if (area < 100):
    print(f"Sua área é de {area:.2f}m² e seu terreno é POPULAR.")
elif area <= 500:
    print(f"Sua área é de {area:.2f}m² e seu terreno é MASTER.")
else:
    print(f"Sua área é de {area:.2f}m² e o seu terreno é VIP.")