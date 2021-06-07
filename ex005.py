print('Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor')
n = int(input('Digite um número para saber seu antecessor e o seu sucessor: '))
a = n-1
s = n+1
print('Analisando o número {}, o seu antecessor é {} e o seu sucessor é {})'.format(n, a, s))

#outra forma do print seria esse abaixo, porém o primeiro seria melhor caso eu precisaria usar o antecessor ou sucessor
# mais a frente no programa, pois teria que ter as variaveis declaradas, coisa que não no segundo exemplo.

# n = int(input('Digite um número para saber seu antecessor e o seu sucessor: '))
# print('Analisando o número {}, O seu antecessor é {} e o seu sucessor é {})'.format(n, (n-1), (n+1)))
