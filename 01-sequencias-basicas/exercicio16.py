# Escreva um programa para calcular a redução do tempo de vida de um fumante. 
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
# # Considere que um fumante perde 10 min de vida a cada cigarro. 
# Calcule quantos dias de vida um fumante perderá e exibia o total em dias.

# Solicita ao usuário a quantidade de cigarros fumados por dia
cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))

# Solicita ao usuário a quantidade de anos que ele já fumou
anos_fumados = int(input("Quantos anos você já fumou? "))

# Calcula o total de cigarros fumados ao longo dos anos
total_cigarros = cigarros_por_dia * 365 * anos_fumados

# Calcula a perda total de vida em minutos (10 minutos por cigarro)
perda_vida_minutos = total_cigarros * 10

# Converte a perda de vida de minutos para dias
perda_vida_dias = perda_vida_minutos / (24 * 60)

# Exibe o total de dias de vida perdidos
print(f"Você perde aproximadamente {perda_vida_dias:.2f} dias de vida devido ao fumo.")

print("\nLembre-se: parar de fumar pode melhorar sua saúde e aumentar sua expectativa de vida!")
print("=====================FIM DO PROGRAMA=====================")
