Algoritmo "exercicio19"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Gustavo Guanabara
// Descrição   : Média do aluno por aproveitamento
// Autor(a)    : Caroline Santos
// Data atual  : 27/08/2026
Var
   nome: Inteiro
   nota1, nota2, media: Real

Inicio
      EscrevaL("------------- MÉDIA DO ALUNO -------------")
      Escreva("Informe o seu nome: ")
      Leia(nome)
      Escreva("Digite sua primeira nota: ")
      Leia(nota1)
      Escreva("Digite sua segunda nota: ")
      Leia(nota2)
      media <- (nota1 + nota2) / 2
      EscrevaL("Sua média é:",media)
      
      Se media > 7 então
         EscrevaL("Você teve média de ",media," e teve um bom aproveitamento.")
      Senao
         EscrevaL("Você teve media de",media," e não teve um bom aproveitamento.")
      FimSe

Fimalgoritmo