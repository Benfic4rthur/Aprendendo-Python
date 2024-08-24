# operador logico and
entrada = input('entrar? [s/n] ')
senha = input('senha? ')
if entrada == 's' and senha != '':
    print('Entrou')
elif entrada == 's' and senha == '':
    print('Favor informar a senha')
else:
    print('Sair')