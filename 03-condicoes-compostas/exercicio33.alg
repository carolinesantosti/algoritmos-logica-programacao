Algoritmo "exercício33"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Gustavo Guanabra
// Descrição   : Algoritmo para aprovar ou não empréstimo bancário.
// Autor(a)    : Caroline Santos
// Data atual  : 18/09/2026
Var
   valor_casa, salario, prestacao: Real
   anos: Inteiro
Inicio
   Escreva("Qual o valor da casa? ")
   Leia(valor_casa)
   Escreva("Qual o seu salário? ")
   Leia(salario)
   Escreva("Você vai pagar em quantos anos? ")
   Leia(anos)
   prestacao <- (valor_casa / (anos * 12))
   Se (prestacao > (salario * 0.3)) entao
      EscrevaL("FINANCIAMENTO NEGADO!!!")
      EscrevaL("O valor da mensalidade seria de ",prestacao:6:2)
   Senao
      EscrevaL("PARABÉNS! SEU FINANCIAMENTO FOI APROVADO!!!")
      EscrevaL("O valor mensal do financiamento é de R$", prestacao:6:2)
   FimSe
Fimalgoritmo