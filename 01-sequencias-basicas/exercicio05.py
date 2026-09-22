# Faça um programa que leia as duas notas de um aluno em uma matéria e mostre na tela a sua média na disciplina.
# Ex:
# Digite a primeira nota: 7.5
# Digite a segunda nota: 8.0
# A média entre 7.5 e 8.0 é 7.75.

nota1 = float(input("Digite a primeira nota: \n"))
nota2 = float(input("Digite a segunda nota: \n"))
media = (nota1 + nota2) / 2
print(f"A média entre {nota1} e {nota2} é {media:2.2f}.")