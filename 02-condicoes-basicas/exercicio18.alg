Algoritmo "exercicio18"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Gustavo Guanabara
// Descrição   : Algoritmo se tem idade para votar ou não.
// Autor(a)    : Caroline Santos
// Data atual  : 27/08/2026
Var
   ano_nasc, idade: Inteiro

Inicio
      Escreval("------------- CÁLCULO PARA VOTAR OU NÃO ------------")
      Escreva("Em que ano você nasceu? ")
      Leia(ano_nasc)
      idade <- (2026 - ano_nasc)

      Se idade >= 18 entao
           Escreva("Você tem",idade," anos e pode votar.")
      Senao
           Escreva("Você tem",idade," anos e não tem idade suficiente para votar.")
      FimSe
      
Fimalgoritmo