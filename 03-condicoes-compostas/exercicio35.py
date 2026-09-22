# Uma empresa de aluguel de carros precisa cobrar pelos seus serviços.
# O aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para carro de luxo.
# Além disso, o cliente paga por Km percorrido. Faça um programa que leia o tipo de carro alugado (popular ou luxo),
# quantos dias de aluguel e quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a tabela a seguir.

print("\033[1;33m----------| LOCADORA DE CARROS |---------\033[m")

# Entrada dos dados
print("Escolha o tipo de carro alugado.")       
print("[1] Carro Popular")
print("[2] Carro de Luxo")

carro_tipo = int(input("Opção desejada: "))
dias = int(input("Quantos dias de aluguel: "))
km = float(input("Quantos Km foram percorridos:"))

# Estrutura de validação e cálculo
if carro_tipo == 1:
    preco_diarias = dias * 90
    if km <= 100:
        preco_km = km * 0.20
    else:
        preco_km = km * 0.10
elif carro_tipo == 2:
    preco_diarias = dias * 150
    if km <= 200:
        preco_km = km * 0.30
    else:
        preco_km = km * 0.25

# Se digitar qualquer outro número, cairá aqui
else:
    preco_diarias = None
    print("ERRO: Opção de carro inválida!")

# Só faz a soma e mostra o resultado se o carro for válido
if preco_diarias is not None:
    total_pagar = preco_diarias + preco_km
    print(f"O valor total do aluguel ficou em: R${total_pagar:.2f}")
