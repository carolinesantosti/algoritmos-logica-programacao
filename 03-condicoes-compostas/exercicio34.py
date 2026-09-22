# O Índice de Massa Corpórea (IMC) é um valor claculo baseado na altura e no peso de uma pessoa.
# De acordo com o valor do IMC, podemos classificar o indivíduo dentro de certas faixas.
# - Abaixo de 18.5: Anaixo do peso.
# - Entre 18.5 e 25: Peso ideal
# - Entre 25 e 30: Sobrepeso
# - Entre 30 e 40: Obesidade
# - Acima de 40: Obesidade mórbida
# OBS.: O IMC é calculado pela expressão peso / altura² (peso dividido pelo quadrado da altura)

# Entrada dos dados
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m) - ex: 1.70: "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Verifica as condições de classificação dos tipos e mostra o resultado do IMC.
if (imc < 18.5):
    print(f"Seu IMC é {imc:.2f}. E você está ABAIXO DO PESO.")
elif (imc >= 18.5) and (imc < 25):
    print(f"Seu IMC é {imc:.2f}. E você está com o PESO IDEAL.")
elif (imc >= 25) and (imc < 30):
    print(f"Seu IMC é {imc:.2f}. E você está com SOBREPESO.")
elif (imc >= 30) and (imc < 40):
    print(f"Seu IMC é {imc:.2f}. E você está com OBESIDADE.")
else:
    print(f"Seu IMC é {imc:.2f}. E você esta com OBESIDADE MÓRBIDA.")