Algoritmo "exercicio36"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Gustavo Guanabra
// Descrição   : Calcula pontos e faturamento com base em horas de atividade
// Autor(a)    : Caroline Santos
// Data atual  : 20/09/2026
Var
   // Seção de Declarações das variáveis
   horas, dinheiro, pontos: real

Inicio
   // 1. Entrada dos dados
   escreva("Quantas horas de atividade você fez no mês? ")
   leia(horas)

   // 2. Estrutura Condicional (Definição dos pontos)
   se (horas <= 10) entao
      pontos <- horas * 2
   senao
      se (horas <= 20) entao
         pontos <- horas * 5
      senao
         pontos <- horas * 10
      fimse
   fimse

   // 3. Cálculo do dinheiro
   dinheiro <- pontos * 0.05
   
   // 4. Saída de dados
   escreva("Você obteve",pontos," pontos e faturou R$",dinheiro:5:2)
Fimalgoritmo