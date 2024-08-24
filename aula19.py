# operador logico or
entrada = input('entrar? [s/n] ')
if entrada == 's' or entrada == 'S':
    senha = input('senha? ')
    if senha != '':
        print('Entrou')
    else:
        print('Favor informar a senha')
else:
    print('Não entrou')