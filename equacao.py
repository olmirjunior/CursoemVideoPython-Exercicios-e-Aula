print('Calculando Equação do Segundo Grau')
a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
delta = (b**2)+4*a*c
print('▲ = Ax² + Bx + C = 0')
print('▲ = {}² - 4 x {} X {} = 0'.format(b, a, c))
print('▲ = {}'.format(delta))
print()
print('Com o valor de ▲ calculado, vamos calcular o valor de X1 e X2')
print('A formula é (X = -B +- √▲) / (2 x A)')
print()
print('Calculando X1')
print('X1 = ({} + {}) / (2 X {})'.format(b, delta ** (1/2), a))
print('X1 = {} / {}'.format(-b + delta ** (1/2), 2 * a))
x1 = (-b + delta ** (1/2)) / (2 * a)
print('X1 = {:.2f}'.format(x1))
print()
print('Calculando X2')
print('X2 = ({} - {}) / (2 X {})'.format(b, delta ** (1/2), a))
print('X2 = {} / {}'.format(-b - delta ** (1/2), 2 * a))
x2 = (-b - delta ** (1/2)) / (2 * a)
print('X2 = {:.2f}'.format(x2))




