print('Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.')

# real = float(input('Digite quanto de dinheiro você tem na carteira R$: '))
# c = 3.27
# print('Você conseguirá comprar US$: {:.2f} Doláres'.format(real/c))

real = float(input('Quanto dinheiro você tem na carteira R$: '))
dolar = real / 3.27
euro = real / 5.15
print('Com R${:.2f} você pode comprar US${:.2f} ou pode comprar €{:.2f}'.format(real, dolar, euro))