from datetime import date
print('')
print('☼ ☽ ' * 20)
print('')
ano = int(input('Digite um ano para saber se ele é um ano BISSESTO ou digite 0 para saber o ano atual: '))
if ano == 0:
    ano = date.today().year
if (ano % 4) == 0 and ano % 100 !=0 or ano % 400 ==0:
    print('O ano de {} é um ano BISSESTO'.format(ano))
else:
    print('O ano de {} NÃO é um ano BISSESTO'.format(ano))
print('')
print('☼ ☽ ' * 20)
