print('Olá, Mundo')
print('\033[1;31;43mOlá, Mundo')
print('\033[0;31;43mOlá, Mundo')
print('\033[1;31;43mOlá, Mundo\033[m')
print('\033[4;30;45mOlá, Mundo\33[m')
print('\033[30mOlá, Mundo')
print('\033[37mOlá, Mundo')
print('\033[7;30mOlá, Mundo')
print('\033[0;33;44mOlá, Mundo\33[m')
print('\033[7;33;44mOlá, Mundo\33[m')

a = 3
b = 5
print('Os valores são \033[033m{} e \033[031m{}'.format(a, b))
print('Os valores são \033[032m{}\033[m e \033[031m{}\033[m!!!'.format(a, b))

nome = 'Olmir Junior'

cores = {'limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m', 'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'],nome, cores['limpa']))
