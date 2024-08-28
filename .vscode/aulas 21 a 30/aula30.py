numero = input('Digite um número: ')

if numero == '':
    print('Nenhum número foi digitado')
else:
    try:
        passanumparanum = int(numero)
        verificanumero = passanumparanum % 2

        if verificanumero == 0:
            print('O número digitado é par')
        else:
            print('O número digitado é ímpar')
    except ValueError:
        try:
            float(numero)
            print('Só são aceitos números inteiros.')
        except ValueError:
            print('Número inválido')
