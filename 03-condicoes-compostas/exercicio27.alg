Algoritmo "exercicio27"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Gustavo Guanabara
// Descrição   : Mostrar a média do aluno e saber se foi Aprovado, Reprovado
//               ou Recuperação
// Autor(a)    : Caroline Santos
// Data atual  : 30/08/2026
Var
   nota1, nota2, media: Real

Inicio
      Escreva("Informe sua primeira nota: ")
      Leia(nota1)
      Escreva("Informe sua segunda nota: ")
      Leia(nota2)
      media <- (nota1 + nota2) / 2
      
      Se (media <= 4.9) entao
         Escreva("Média até 4.9: REPROVADO!")
      Senao
           Se (media >= 5) e (media <= 6.9) entao
              Escreva("Média entre 5.0 e 6.9: RECUPERAÇÃO!")
           Senao
                Se (media >= 7) entao
                Escreva("Média 7.0 ou superior: APROVADO!")
                FimSe
           FimSe
      FimSe
Fimalgoritmo