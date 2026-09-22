# Um programa de vida saudável quer dar pontos atividades físicas que podem ser trocados por dinheiro. 
# O sistema funciona assim:
# - Cada hora de atividade física no mês vale pontos
# - até 10h de atividade no mês: ganha 2 pontos por hora.
# - de 10h até 20h de atividade no mês: ganha 5 pontos por hora
# - acima de 20h de atividade no mês: ganha 10 pontos por hora
# - a cada ponto ganho, o cliente fatura R$0,05 (5 centavos)
# Faça um programa que leia quantas horas de atividade uma pessoa teve por mês, calcule e mostre quantos pontos ela teve 
# e quanto dinheiro ela conseguiu ganhar.

print("\033[1;36m----------| VIDA SAUDÁVEL |---------\033[m")

# Entrada dos dados
horas = float(input("Quantas horas de atividade física você fez no mês: "))

# Estrutura condicional para definição dos pontos
if horas <= 10:
    pontos = horas * 2
elif horas <= 20:
    pontos = horas * 5
else:
    pontos = horas * 10

# Cálculo do dinheiro
dinheiro = pontos * 0.05

# Saída dos dados
print(f"Você obteve {pontos} pontos e faturou R${dinheiro:.2f}.")
