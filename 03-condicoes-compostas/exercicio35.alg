Algoritmo "exercicio35"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Gustavo Guanabara
// Descrição   : Algoritmo aluguel de carros
// Autor(a)    : Caroline Santos
// Data atual  : 19/09/2026
Var
   carro_tipo, dias: Inteiro
   km, preco_diarias, preco_km, total_pagar: Real

Inicio
   // Entrada dos dados com Menu Numérico
   Escreval("--- LOCADORA DE VEÍCULOS ---")
   Escreval(" Escolha o tipo de carro alugado:")
   Escreval(" [1] Carro Popular")
   Escreval(" [2] Carro de Luxo")
   Escreva(" Opção desejada: ")
   Leia(carro_tipo)
   Escreva("Quantos dias de aluguel: ")
   Leia(dias)
   Escreva("Quantos KM foram percorridos: ")
   Leia(km)

   Se (carro_tipo = 1) entao
      preco_diarias <- dias * 90
      Se (km <= 100) entao
         preco_km <- km * 0.20
      Senao
         preco_km <- km * 0.10
      FimSe
   Senao // Se não for 1, o programa assume direto que é o de Luxo
      preco_diarias <- dias * 150
      Se (km <= 200) entao
         preco_km <- km * 0.30
      Senao
         preco_km <- km * 0.25
      FimSe // Fecha os km do luxo
   FimSe // Fecha o bloco principal

   total_pagar <- preco_diarias + preco_km
   Escreval("O valor total do aluguel ficou em: R$", total_pagar:6:2)
Fimalgoritmo