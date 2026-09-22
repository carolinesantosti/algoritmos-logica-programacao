Algoritmo "exercicio25"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Gustavo Guanabra
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Caroline Santos
// Data atual  : 29/08/2026
Var
   reta1, reta2, reta3: real

Inicio
   Escreva("Digite o primeiro valor da reta: ")
   Leia(reta1)
   Escreva("Digite o segundo valor da reta: ")
   Leia(reta2)
   Escreva("Digite o terceiro valor da reta: ")
   Leia(reta3)
   EscrevaL("---------------------------------------------")
   Se (reta1 < (reta2 + reta3)) e (reta2 < (reta1 + reta3)) e (reta3 < (reta1 + reta2)) entao
      EscrevaL("É possível formar um triângulo!")
      Se (reta1 = reta2) e (reta2 = reta3) entao
         EscrevaL("O triângulo é EQUILÁTERO.")
      Senao
         Se (reta1 = reta2) ou (reta2 = reta3) ou (reta1 = reta3) entao
            EscrevaL("O triângulo é ISÓSCELES.")
         Senao
            EscrevaL("O triângulo é ESCALENO.")
         FimSe
      FimSe
   Senao
      Escreva("NÃO é possível formar um triângulo!")
   FimSe
Fimalgoritmo