# Faça um algoritmo que leia a largura e altura de uma parede. Calcule e mostre a área a ser pintada e a quantidade de tinta necessária para  serviço.
# Sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input("Digite a largura da parede (em metros): "))
altura = float(input("Digite a altura da parede (em metros): "))

area = largura * altura
tinta_necessaria = area / 2

print(f"A área a ser pintada é de {area:.2f} metros quadrados.")
print(f"Você precisará de {tinta_necessaria:.2f} litros de tinta.")