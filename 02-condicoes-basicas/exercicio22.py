# Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua situação em relação ao alistamento militar.
# Se estiver antes dos 18 anos, mostre em quantos anos faltam para o alistamento.
# Se já tiver 18 anos, mostre quantos anos já se passaram desde o alistamento.

print("===== VERIFICADOR DE ALISTAMENTO MILITAR =====\n")
# Solicita ao usuário que insira o ano de nascimento
ano_nascimento = int(input("Digite o ano de nascimento: "))

# Calcula a idade atual do rapaz
ano_atual = 2026  # Você pode substituir pelo ano atual dinamicamente usando datetimef
idade = ano_atual - ano_nascimento

# Verifica a situação em relação ao alistamento militar
if idade < 18:
    anos_faltando = 18 - idade
    print(f"O rapaz tem {idade} anos. Faltam {anos_faltando} anos para o alistamento militar.")
elif idade == 18:
    print(f"O rapaz tem {idade} anos. Ele deve se alistar este ano.")
else:
    anos_passados = idade - 18
    print(f"O rapaz tem {idade} anos. Já se passaram {anos_passados} anos desde o alistamento militar.")