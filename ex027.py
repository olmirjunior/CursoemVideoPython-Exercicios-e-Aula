n = str(input('Digite o nome completo: ')).strip()
nome = n.split()
print('Muito prazar em te conhecer {}'.format(nome[0]))
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu ultimo nome é: {}'.format(nome[len(nome)-1]))

