Algoritmo "exercicio6"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Antecessor e Sucessor de um número digitado pelo usuário
// Autor(a)    : Caroline Santos
// Data atual  : 18/08/2026
Var
   num, ant, suc: inteiro

Inicio
      escreva ("Digite um número: ")
      leia (num)
      
      ant <- num -1
      suc <- num +1
      
      escreval ("O antecessor de",num, " é igual",ant)
      escreval ("O sucessor de",num, " é igual", suc)

Fimalgoritmo