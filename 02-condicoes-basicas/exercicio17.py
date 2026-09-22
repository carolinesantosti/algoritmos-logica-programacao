# Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. 
# Nesse caso, exiba o valor da multa, cobrando R$ 5 por cada km acima de 80 km/h.

print("===== CALCULADORA DE MULTA DE VELOCIDADE =====\n")
# Solicita ao usuário a velocidade do carro
velocidade = float(input("Digite a velocidade do carro (km/h): "))
print(f"Velocidade informada: {velocidade} km/h")
print("===============================================")

# Verifica se a velocidade ultrapassa 80 km/h
if velocidade > 80:
    print("Você foi multado!")
    multa = (velocidade - 80) * 5
    print(f"Valor da multa: R$ {multa:.2f}")
else:
    print("Você está dentro do limite de velocidade. Boa viagem!")
print("\n=============== FIM DO PROGRAMA ================")
