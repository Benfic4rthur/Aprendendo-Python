nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

if nome == '' and idade == '':
    print('Nome e idade vazios')
elif nome == '':
    print('Nome vazio')
elif idade == '':
    print('Idade vazia')
else:
    print('Nome:', nome)
    print('Idade:', idade)
    print('Seu nome invertido é {}'.format(nome[::-1]))
    print('Seu nome possui espaços? {}'.format(' ' in nome))
    print('Seu nome tem {} letras'.format(len(nome)))
    print('A primeira letra do seu nome e {}'.format(nome[0]))
    print('A ultima letra do seu nome e {}'.format(nome[-1]))