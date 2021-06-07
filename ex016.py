import math

num = float(input('Digite um valor: '))
inteiro = math.trunc(num)
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, inteiro))

# Duas opçoes para resolver o mesmo problema

num1 = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num1, int(num1)))

