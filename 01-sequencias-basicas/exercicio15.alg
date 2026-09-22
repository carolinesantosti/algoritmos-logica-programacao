Algoritmo "exercicio15"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Dias trabalhados
// Autor(a)    : Caroline
// Data atual  : 21/08/2026
Var
   dias_trabalhados: inteiro
   horas_trabalhadas,salario: real

Inicio
      escreva("Digite quantos dias você trabalhou: ")
      leia(dias_trabalhados)
      
      horas_trabalhadas <- dias_trabalhados * 8
      salario <- horas_trabalhadas * 25
      escreva("O seu salário é: R$", salario:0:2)

Fimalgoritmo