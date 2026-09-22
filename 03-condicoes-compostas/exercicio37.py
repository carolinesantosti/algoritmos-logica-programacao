# Uma empresa precisa reajustar o salário dos seus funcionários, dando um aumento de acordo com alguns fatores. 
# Faça um programa que leia o salário atual, o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa. 
# No final, mostre o seu novo salário, baseado na tabela a seguir: 

# Mulheres
#- menos de 15 anos de empresa: +5%
#- de 15 até 20 anos de empresa: +12%
#- mais de 20 anos de empresa: +23%

# Homens
#- menos de 20 anos de empresa: +3%
#- de 20 até 30 anos de empresa: +13%
#- mais de 30 anos de empresa: +25%

# Exibe o título do programa em amarelo e restaura a cor do terminal.
print("\033[1;33m----------| REAJUSTE SALARIAL |---------\033[m")

# 1. ENTRADA DE DADOS
# Solicita o salário atual e converte o valor informado para float.
salario = float(input("Informe seu salário atual: R$"))

# Solicita o gênero e converte a resposta para maiúscula.
# Assim, tanto "f" quanto "F" serão reconhecidos como "F".
genero = input("Informe seu gênero [M/F]: ").upper()

# Solicita o tempo de empresa e converte a resposta para inteiro.
anos = int(input("Quantos anos você trabalha na empresa? "))

# Exibe uma linha para separar a entrada de dados do resultado.
print("----------------------------------------------")


# 2. DEFINIÇÃO DO PERCENTUAL DE REAJUSTE
# Verifica o gênero para identificar qual conjunto de regras será utilizado.

if genero == "F":

    # Para F: menos de 15 anos recebe reajuste de 5%.
    if anos < 15:
        reajuste = 0.05

    # De 15 até 20 anos recebe reajuste de 12%.
    elif anos <= 20:
        reajuste = 0.12

    # Acima de 20 anos recebe reajuste de 23%.
    else:
        reajuste = 0.23

elif genero == "M":

    # Para M: menos de 20 anos recebe reajuste de 3%.
    if anos < 20:
        reajuste = 0.03

    # De 20 até 30 anos recebe reajuste de 13%.
    elif anos <= 30:
        reajuste = 0.13

    # Acima de 30 anos recebe reajuste de 25%.
    else:
        reajuste = 0.25

# Se o gênero não for F nem M, informa que a opção é inválida.
else:
    print("ERRO! Gênero INVÁLIDO! Digite M ou F.")


# 3. CÁLCULO DO REAJUSTE SALARIAL
# Só executa os cálculos se o gênero informado for válido.
if genero == "F" or genero == "M":

    # Calcula o valor do aumento em reais.
    valor_aumento = salario * reajuste

    # Soma o aumento ao salário original para obter o novo salário.
    novo_salario = salario + valor_aumento


    # 4. EXIBIÇÃO DOS RESULTADOS
    # Mostra o tempo de empresa informado pelo funcionário.
    print(f"Tempo de Empresa: {anos} anos")

    # Exibe o percentual de reajuste sem casas decimais.
    # O formato .0% transforma, por exemplo, 0.12 em 12%.
    print(f"Reajuste: {reajuste:.0%}")

    # Exibe o valor do aumento no padrão monetário brasileiro.
    # :,.2f adiciona o separador de milhares e duas casas decimais.
    # Os três replace() trocam os separadores para o padrão brasileiro.
    print(f"Valor do aumento: R$ {valor_aumento:,.2f}".replace(",", "x").replace(".", ",").replace("x", "."))

    # Exibe o novo salário com a mesma formatação monetária.
    print(f"Seu novo salário é de R$ {novo_salario:,.2f}".replace(",", "x").replace(".", ",").replace("x", "."))
