import math

print('Faça um programa que leia um ângulo qualquer e mostre na tela o valor do SENO, COSSENO E TANGENTE, desse ângulo.')
angulo = float(input('Digite o angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {:.2f} tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {:.2f} tem a TANGENTE de {:.2f}'.format(angulo, tangente))







