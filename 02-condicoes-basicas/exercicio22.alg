Algoritmo "exercicio22"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Gustavo Guanabara
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 28/08/2026
Var
   ano_nascimento, idade, anos_faltando, anos_passados: Inteiro


Inicio
   EscrevaL("------ VERIFICADOR DE ALISTAMENTO MILITAR ------")
   Escreva("Digite o ano de nascimento: ")
   Leia(ano_nascimento)
   idade <- (2026 - ano_nascimento)

   Se (idade < 18) entao
      anos_faltando <- (18 - idade)
      EscrevaL("Você tem",idade," anos e faltam", anos_faltando," ano(s) para o alistamento.")
   Senao
      Se (idade > 18) entao
         anos_passados <- idade - 18)
         Escreva("Já se passaram", anos_passados, " anos desde o alistamento militar.")
      Senao
         Se (idade = 18) entao
            Escreva("Você deve se alistar esse ano.")
         FimSe
      FimSe
   FimSe
Fimalgoritmo