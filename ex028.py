# import random
# jogador = int(input('Digite um número entre 0 e 5: '))
# computador = random.randint(0, 5)
# print('O número escolhido pelo computador foi {}'.format(computador))
# if jogador == computador:
#     print('Você venceu!')
# else:
#     print('Você perdeu!')

# O programa acima foi escrito por mim e está funcionando.
# O programa abaixo foi escrito pelo professor.

import random
from time import sleep
computador = random.randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
print('')
if jogador == computador:
    print('PARABÉNS! Você GANHOU, pois eu também pensei no número {}'.format(jogador))
else:
    print('HAHAHA, você PERDEU, pois eu pensei no número {} e não no número {}, boa sorte na próxima vez'. format(computador, jogador))
