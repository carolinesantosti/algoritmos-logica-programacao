# DESAFIO: Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais
# - ESCALENO: todos os lados diferentes

# Solicita o usuário que informe os valores da reta
reta1 = float(input("Digite o primeiro valor da reta: "))
reta2 = float(input("Digite o segundo valor da reta: "))
reta3 = float(input("Digite o terceiro valor da reta: "))

# Verifica se é possível formar ou não o triângulo
if (reta1 < (reta2 + reta3)) and (reta2 < (reta1 + reta3)) and (reta3 < (reta1 + reta2)):
    print("É possível formar um triângulo!")

    # Verifica qual o tipo de triângulo
    if reta1 == reta2 == reta3:
        print("O triângulo é EQUILÁTERO.")
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print("O triângulo é ISÓSCELES.")
    else:
        print("O triângulo é ESCALENO.")
else:
    print("Não é possível formar um triângulo")