Algoritmo "exercicio28"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Gustavo Guanabara
// Descrição   : Mostrar a comprimento de um terreno e classificar sua área
//               total.
// Autor(a)    : Caroline Santos
// Data atual  : 02/09/2026

Var
   largura, comprimento, area: Real

Inicio
   Escreva("Informe a largarua do terreno em m²: ")
   Leia(largura)
   Escreva("Informe o comprimento do terreno em m²: ")
   Leia(comprimento)
   area <- largura * comprimento

   Se (area < 100) entao
      Escreva("Sua área é de ",area:5:2, "m² e o seu terreno é POPULAR.")
   Senao
      Se (area <= 500) entao
         Escreva("Sua área é de ",area:5:2, "m² e o seu terreno é MASTER.")
      Senao
         Escreva("Sua área é de ",area:5:2, "m² e o seu terreno é VIP.")
      FimSe
   FimSe
Fimalgoritmo