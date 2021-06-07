import math

print('Faça um programa que leia o comprimento de cateto \noposto e do cateto adjacente de um triangulo retangulo.\nCalcule e mostre o comprimento da hipotenusa')
print('◣')
catoposto = float(input('Qual o comprimento do CATETO OPOSTO: '))
catadjacente = float(input('Qual o comprimento do CATETO ADJACENTE: '))
hip = math.hypot(catoposto, catadjacente)
print('A hipotenusa é {:.2f}'.format(hip))


# outra opção para este exercicio (uma formula matematica)

#
# catoposto = float(input('Qual o comprimento do CATETO OPOSTO: '))
# catadjacente = float(input('Qual o comprimento do CATETO ADJACENTE: '))
# hip = (catoposto ** 2 + catadjacente **2) ** (1/2)
# print('A Hipotenusa é {:.2f}'.format(hip))
