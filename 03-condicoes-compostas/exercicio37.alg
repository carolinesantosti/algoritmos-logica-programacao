Algoritmo "exercicio37"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Gustavo Guanabara
// Descrição   : Cálculo para reajuste de salário
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 21/09/2026
Var
   salario, novo_salario: Real
   genero: caractere
   anos: inteiro

Inicio
   // 1. Entrada de dados
   EscrevaL("---------- | REAJUSTE DE SALÁRIO | -----------")
   Escreva("Informe seu salário atual: R$")
   Leia(salario)

   Escreva("Informe seu gênero (M ou F): ")
   Leia(genero)

   Escreva("Quantos anos você trabalha na empresa? ")
   Leia(anos)

   // 2. Validação do gênero
   Se (genero = "F") ou (genero = "M") entao

      // 3. Verifica as condições de reajuste
      Se (genero = "F") entao

         Se (anos < 15) entao
            novo_salario <- salario * 1.05
         Senao
            Se (anos <= 20) entao
               novo_salario <- salario * 1.12
            Senao
               novo_salario <- salario * 1.23
            FimSe
         FimSe

      Senao
         Se (anos < 20) entao
            novo_salario <- salario * 1.03
         Senao
            Se (anos <= 30) entao
               novo_salario <- salario * 1.13
            Senao
               novo_salario <- salario * 1.25
            FimSe
         FimSe
      FimSe

      // 4. Saída do resultado
      EscrevaL("Seu novo salário é de R$", novo_salario:5:2)

   Senao
      EscrevaL("ERRO: gênero inválido! Digite M ou F.")
   FimSe
Fimalgoritmo