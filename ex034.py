nome = str(input('Digite o nome do funcioário: '))
salario = float(input('Qual o salário do funcionário R$ '))
sal10 = (salario * 10 / 100)
sal15 = (salario * 15 / 100)
if (salario >= 1250) * (10 * 10 / 100):
    print('O novo salário do funcionário(a) {} com 10% de aumento será de {}'.format(nome, sal10 + salario))
else:
    print('O novo salário do funcionário(a) {} com 15% de aumento será de {}'.format(nome, sal15 + salario))

# Neu codigo acima, do professor abaixo

salario = float(input('Qual o salário do funcionário R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, novo))