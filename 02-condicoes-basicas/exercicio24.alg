Algoritmo "exercicio24"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Gustavo Guanabara
// Descrição   : Calcular preço da passagem
// Autor(a)    : Caroline Santos
// Data atual  : 29/08/2026
Var
   distancia, preco: Real

Inicio
   EscrevaL("============= Passagem de Ônibus ==============")
   Escreva("Qual a distância que deseja percorrer? [Km] ")
   Leia(distancia)
   EscrevaL("===============================================")
   Se (distancia <= 200) entao
      preco <- (distancia * 0.5)
      EscrevaL("O preço da passagem é de R$",preco:5:2)
   Senao
      preco <- (distancia * 0.45)
      EscrevaL("O preço da passagem é de R$",preco:5:2)
   FimSe
Fimalgoritmo