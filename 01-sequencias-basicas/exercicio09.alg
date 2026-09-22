Algoritmo "exercicio9"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Mostrar quantos dólares o usuário pode comprar com base em reais
// Autor(a)    : Caroline Santos
// Data atual  : 19/08/2026
Var
   dinheiro, dolar: real

Inicio
      escreva ("Quantos reais você tem na sua carteira: R$")
      leia (dinheiro)
      dolar <- dinheiro / 3.45
      escreva ("Você pode comprar U$", dolar:5:2)

Fimalgoritmo