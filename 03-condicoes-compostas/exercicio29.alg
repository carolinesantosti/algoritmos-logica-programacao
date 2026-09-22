Algoritmo "exercicio29"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Gustavo Guanabara
// Descrição   : Cálculo de um novo salário de acordo com as condições previstas.
// Autor(a)    : Caroline Santos
// Data atual  : 03/09/2026
Var
   nome: Caractere
   salario_atual, salario_novo, anos: Real

Inicio
   EscrevaL("========= CÁLCULO NOVO SALÁRIO ==========")
   Escreva("Informe o seu nome: ")
   Leia(nome)
   Escreva("Agora informe o seu salário: R$")
   leia(salario_atual)
   Escreva("Informe também quanto tempo você trabalha na nossa empresa: ")
   Leia(anos)

   Se (anos <= 3) entao
      salario_novo <- salario_atual * 1.03
      Escreva(nome,", você recebeu um aumento de 3% e seu novo salário é de R$",salario_novo:5:2)
   Senao
      Se (anos <= 10) entao
         salario_novo <- salario_atual * 1.125
         Escreva(nome,", você recebeu um aumento de 12.5% e seu novo salário é de R$",salario_novo:5:2)
      Senao
         salario_novo <- salario_atual * 1.2
         Escreva(nome,", você recebeu um aumento de 20% e seu novo salário é de R$",salario_novo:5:2)
      FimSe
   FimSe
Fimalgoritmo