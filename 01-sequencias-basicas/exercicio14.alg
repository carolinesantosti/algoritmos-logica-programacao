Algoritmo "exercicio14"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aluguel de carro e km percorridos
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 20/08/2026
Var
   qntd_km, preco_total: real
   qntd_dias: inteiro

Inicio
  escreva("Quantos kilômetros o carro foi percorrido? ")
  leia(qntd_km)
  escreva("Quantos dias você alugou o carro? ")
  leia(qntd_dias)
  
  preco_total <- (qntd_dias * 90) + (qntd_km * 0.20)
  
  escreva("O valor total do aluguel do carro é de: R$",preco_total:5:2)
  
Fimalgoritmo