Algoritmo "exercicio23"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Gustavo Guanabara
// Descrição   : Saber o nome, sexo e valor de uma compra e
//               assim dar um desconto
// Autor(a)    : Caroline Santos
// Data atual  : 28/08/2026

Var
   nome, sexo: Caractere
   desconto, valor, valor_final: Real

Inicio
   EscrevaL("------------ LOJAS CAROL ------------")
   Escreva("Qual o seu nome: ")
   Leia(nome)
   Escreva("Informe seu sexo [M/F]: ")
   Leia(sexo)
   Escreva("Qual foi o valor da compra: R$")
   Leia(valor)

   EscrevaL("--------------------------------------")
   Se (sexo = "M") entao
      desconto <- (valor * 0.05)
      valor_final <- (valor - desconto)
      EscrevaL("Você recebeu um desconto de 5%.")
      EscrevaL("O valor final das suas compras é: R$", valor_final:5:2)
   Senao
      desconto <- (valor * 0.13)
      valor_final <- (valor - desconto)
      EscrevaL("Você recebeu um desconto de 13%.")
      EscrevaL("O valor final das suas compras é: R$", valor_final:5:2)
   FimSe

Fimalgoritmo
