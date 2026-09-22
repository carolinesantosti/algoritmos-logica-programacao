Algoritmo "exercicio10"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Calcular a altura e largura de uma área e a qntd da tinta.
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 19/08/2026
Var
   largura, altura, area, qntd_tinta: real

Inicio
      escreva ("Qual a largura da parede? ")
      leia (largura)
      escreva ("Qual a altura da parede? ")
      leia (altura)
      
      // Cálculo da área de superfície
      area <- largura * altura
      
      escreval ("A área da parede a ser pintada é de ",area:4:2," metros quadrados.")
      
      // Cálculo do rendimento da tinta
      qntd_tinta <- area / 2
      escreval ("Você irá precisar de ",qntd_tinta:4:2, " litros de tinta para o serviço.")
      
Fimalgoritmo