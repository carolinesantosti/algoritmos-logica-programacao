# Faça um algoritmo que leia um determinado ano e mostre se ele é bissexto ou não.

print("===== VERIFICADOR DE ANO BISSEXTO =====\n")

# Solicita ao usuário que insira um ano
ano = int(input("Digite um ano: "))

# Verifica se o ano é bissexto usando as regras do calendário gregoriano
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é BISSEXTO.")
else:
    print(f"O ano {ano} NÃO É BISSEXTO.")