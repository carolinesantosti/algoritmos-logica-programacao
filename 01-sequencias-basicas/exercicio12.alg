Algoritmo "exercicio12"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Preço do produto com desconto
// Autor(a)    : Caroline Sants
// Data atual  : 20/08/2026
Var
   preco_original, valor_desconto, preco_final: real

Inicio
   escreva("Qual o preço do produto? ")
   leia(preco_original)
      
   // Aplicando o cálculo
   valor_desconto <- preco_original * 0.05
   preco_final <- preco_original - valor_desconto
   
   escreval("Valor do desconto: R$", valor_desconto:5:2)
   escreval("Preço final a pagar: R$", preco_final:5:2)
   
Fimalgoritmo