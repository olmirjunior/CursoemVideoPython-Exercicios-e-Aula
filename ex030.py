num = int(input('Digite um número inteiro: '))
if (num % 2) == 0:
    print('O número {} é par!'.format(num))
else:
    print('O número {} é impar'.format(num))

# RESOLUÇÃO DO PROFESSOR

numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é par!'.format(num))
else:
    print('O número {} é impar!'.format(num))
