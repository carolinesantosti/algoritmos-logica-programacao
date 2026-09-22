# Crie um programa que leia o tamanho de três segmentos de reta. 
# Analise seus comprimentos e diga se é possível formar um triângulo com essas retas. 
# Matematicamente, para três segmentos formarem um triângulo, o comprimento de cada lado deve ser menor que a soma dos outros dois.

# Solicita o usuário que informe os valores da reta
reta1 = float(input("Digite o primeiro valor da reta: "))
reta2 = float(input("Digite o segundo valor da reta: "))
reta3 = float(input("Digite o terceiro valor da reta: "))

# Verifica se é possível formar ou não o triângulo
if (reta1 < (reta2 + reta3)) and (reta2 < (reta1 + reta3)) and (reta3 < (reta1 + reta2)):
    print("É possível formar um triângulo!")
else:
    print("Não é possível formar um triângulo")