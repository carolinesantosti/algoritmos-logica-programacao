Algoritmo "exercicio11"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Mostrar o valor de Delta
// Autor(a)    : Caroline Santos
// Data atual  : 20/08/2026
Var
   a, b, c, delta: real

Inicio
      escreva("Digite o valor de A: ")
      leia(a)
      escreva("Digite o valor de B: ")
      leia(b)
      escreva("Digite o valor de C: ")
      leia(c)
      
      delta <- (b ^ 2) - (4 * a * c)
      
      escreval("O valor do delta é: ", delta)

Fimalgoritmo