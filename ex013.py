print('Faça um algoritimo que mostre o salário de um funcionário e mostre seu novo salário com 15% de desconto')
# salario = float(input('Qual é o salário do funcionário R$: '))
# aumento = float(input('Digite o percentual do aumento %: '))
# percaumento = (aumento/100)
# novosalario = (salario*percaumento)
# print('Seu novo salário é R$: {}'.format(salario+novosalario))


# 2 opções

salario = float(input('Qual é o salário do funcionário R$ '))
novo = salario + (salario * 15 / 100)
print('O funcionário que ganhava R$ {}, com 15% de aumento o novo salário é de R$ {:.2f}'.format(salario, novo))



