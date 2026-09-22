Algoritmo "exercicio26"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Gustavo Guanabara
// Descrição   : Detectar um número maior que o outro digitado
// Autor(a)    : Caroline Santos
// Data atual  : 30/08/2026
Var
   num1, num2: Inteiro

Inicio
      Escreva("Digite o primeiro número: ")
      Leia(num1)
      Escreva("Digite o segundo número: ")
      Leia(num2)
      
      Se (num1 > num2) entao
         Escreva("O primeiro valor é maior que o segundo valor.")
      Senao
           Se (num2 > num1) entao
              Escreva("O segundo valor é maior que o primeiro valor.")
           Senao
                Escreva("Não existe valor maior, os dois são iguais.")
           FimSe
      FimSe
Fimalgoritmo