n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {}'.format(m))
if m >= 6.0:
    print('Sua média foi boa!')
else:
    print('Sua média foi ruim, Estude mais!')

# ou posso usar este comando abaixo
# print('PARABÉNS' if m >=6 else 'ESTUDE MAIS!')





# nome = str(input('Qual é o seu nome? '))
# if nome == 'Junior':
#     print('Que nome lindo você tem!')
# else:
#     print('Seu nome é tão normal!')
# print('Bom dia, {}'.format(nome))
