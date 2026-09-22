# Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade dela e depois mostre se ela pode ou não votar. 
# (Para votar, a pessoa deve ter pelo menos 16 anos).

print("===== VERIFICADOR DE IDADE PARA VOTO =====\n")
# Solicita ao usuário o ano de nascimento
ano_nascimento = int(input("Digite o ano de nascimento: "))

# Calcula a idade da pessoa
idade = 2026 - ano_nascimento

# Verifica se a pessoa pode votar
if idade >= 16:
    print(f"Você tem {idade} anos e pode votar.")
else:
    print(f"Você tem {idade} anos e não pode votar.")