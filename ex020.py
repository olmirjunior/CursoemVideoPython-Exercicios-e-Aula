import random

print('O mesmo proofessor do exercicio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.\n'
      'Faça um programa que leia o nome dos quatros alunos e mostre a ordem dos sorteados')
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem da apredentação será:')
print(lista)

