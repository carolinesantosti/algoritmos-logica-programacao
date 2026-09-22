Algoritmo "exercicio8"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Conversão de metros para outras medidas
// Autor(a)    : Caroline Santos
// Data atual  : 18/08/2026

Var
   metros, Km, Hm, Dam, dm, cm, mm: real

Inicio
      escreva ("Digite uma distância em metros: ")
      leia (metros)
      Km <- metros / 1000
      Hm <- metros / 100
      Dam <- metros / 10
      dm <- metros * 10
      cm <- metros * 100
      mm <- metros * 1000
      escreval ("A distância de", metros, " metros corresponde a:")
      escreval (Km,"Km")
      escreval (Hm,"Hm")
      escreval (Dam,"Dam")
      escreval (dm,"dm")
      escreval (cm,"cm")
      escreval (mm,"mm")
Fimalgoritmo