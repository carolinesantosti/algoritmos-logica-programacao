Algoritmo "exercicio34"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Gustavo Guanabra
// Descrição   : Cálculo IMC
// Autor(a)    : Caroline Santos
// Data atual  : 19/09/2026
Var
   peso, altura, imc: Real

Inicio
   // Entrada dos dados
   Escreva("Digite seu peso (kg): ")
   Leia(peso)
   Escreva("Digite sua altura (m) - ex: 1.75: ")
   Leia(altura)

   // Cálculo do IMC (altura ao quadrado)
   imc <- peso / (altura * altura)

   // Exibe o resultado
   EscrevaL("Seu IMC é: ",imc:2:2)

   //Estrutura condicional
   Se (imc < 18.5) entao
      Escreva("Classificação: Abaixo do peso.")
   Senao
        Se (imc >= 18.5) e (imc < 25) entao
           Escreva("Classificação: Peso ideal. Parabéns!")
        Senao
             Se (imc >= 25) e (imc < 30) entao
                Escreva("Classificação: Sobrepeso.")
             Senao
                  Se (imc >= 30) e (imc < 40) entao
                     Escreva("Classificação: Obesidade.")
                  Senao
                       Escreva("Classficação: Obesidade Mórbida.")
                  FimSe
             FimSe
        FimSe
   FimSe
Fimalgoritmo