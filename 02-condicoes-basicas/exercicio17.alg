Algoritmo "exercicio17"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Gustavo Guanabara
// Descrição   : Algoritmo pra saber se a velocidade ultrapassou o limite de 80 Km.
// Autor(a)    : Caroline Santos
// Data atual  : 26/08/2026
Var
   velocidade, multa: Real

Inicio
      EscrevaL("-----------------------------------")
      EscrevaL("     VERIFICAÇÃO DE VELOCIDADE     ")
      EscrevaL("-----------------------------------")
      Escreva("Qual foi a velocidade do carro? ")
      Leia(velocidade)
      Se (velocidade) > 80 entao
         EscrevaL("Você foi MULTADO! O limite permitido é de 80 Km.")
         multa <- (velocidade - 80) * 5
         EscrevaL("O valor da multa é de: ", "R$",multa)
      Senao
         Escreva("Limite de velocidade permitido.")
      FimSe
Fimalgoritmo