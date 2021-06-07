velocidade = int(input('Digite a velocidade do carro em KM/H '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Você foi multado por dirigir acima dos 80KM/H'.format(velocidade))
    print('Sua multa será de R$ 7,00 por KM excedido, o Valor de sua multa é de R$ {}'.format(multa))
else:
    print('Parabéns, você dirige com prudência!')




