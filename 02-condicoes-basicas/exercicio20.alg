Algoritmo "exericio20"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Gustavo Guanabara
// Descrição   : Saber se um número é par ou ímpar.
// Autor(a)    : Caroline Santos
// Data atual  : 27/08/2026
Var
   num: Inteiro

Inicio
      EscrevaL("-------- PAR OU ÍMPAR? ----------")
      Escreva("Digite um número: ")
      Leia(num)
      Se (num % 2 = 0) entao
         Escreval("O número",num," é PAR!")
      Senao
         Escreval("O número",num," é ÍMPAR!")
      FimSe
      
Fimalgoritmo