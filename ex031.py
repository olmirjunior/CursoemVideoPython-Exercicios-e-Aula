# viagem = int(input('Qual a distância da viagem em KM: '))
# tarifa1 = 0.45 * viagem
# tarifa2 = 0.50 * viagem
# if viagem >= 200:
#     print('O valor da sua viagem será de R$ {}'.format(tarifa1))
# else:
#     print('O valor da sua viagem será de R$ {}'.format(tarifa2))

# minha resposta acima, abaixo do professor

# distancia = float(input('Qual é a distância da sua viagem? '))
# print('Você está prestes a começar uma viagem de {} KM'.format(distancia))
# if distancia <= 200:
#     preço = distancia * 0.50
# else:
#     preço = distancia * 0.45
# print('O preço da sua passagem será de R$ {:.2f}'.format(preço))

# outra format

distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {} KM'.format(distancia))
preço = distancia * 0.50 if distancia <=200 else distancia * 0.45
print('O preço da sua passagem será de R$ {:.2f}'.format(preço))
