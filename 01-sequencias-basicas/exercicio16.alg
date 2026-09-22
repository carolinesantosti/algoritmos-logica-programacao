Algoritmo "exercicio16"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Redução de tempo de vida de um fumante
// Autor(a)    : Caroline
// Data atual  : 21/08/2026

Var
   cigarros_por_dia, anos_fumados: inteiro
   total_cigarros, minutos_perdidos: inteiro
   dias_perdidos: real

Inicio
      escreva("Quantos cigarros você fuma por dia? ")
      leia(cigarros_por_dia)
      escreva("Há quantos anos você fuma? ")
      leia(anos_fumados)

      //1 ano tem 365 dias
      total_cigarros <- cigarros_por_dia * 365 * anos_fumados

      // Cada cigarro tira 10 minutos de vida
      minutos_perdidos <- total_cigarros * 10

      // Conversão: minutos para horas (/60) e horas para dias (/24)
      dias_perdidos <- minutos_perdidos / 60 / 24

      // Saída de dados
      escreval("--- RESULTADO ---")
      escreval("Total de cigarros fumados: ", total_cigarros)
      escreval("Você perderá aproximadamente ", dias_perdidos:1:1, " dias de vida.")

Fimalgoritmo