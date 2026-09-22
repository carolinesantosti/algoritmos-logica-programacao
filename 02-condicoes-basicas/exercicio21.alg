Algoritmo "exercicio21"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Gustavo Guanabara
// Descrição   : Algoritmo se o ano é Bissexto ou não.
// Autor(a)    : Caroline Santos
// Data atual  : 27/08/2026
Var
   ano: Inteiro

Inicio
      Escreva("Digite um ano: ")
      Leia(ano)
      Se (ano % 4 = 0) e (ano % 100 <> 0) ou (ano % 400 = 0) entao
         Escreval("O ano ", ano, " é BISSEXTO!")
      Senao
         Escreval("O ano ", ano, " NÃO É BISSEXTO!")
      FimSe

Fimalgoritmo