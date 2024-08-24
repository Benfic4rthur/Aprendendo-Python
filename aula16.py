# if / elif       / else
# se / se não se / se não

entrada = int(input('Qual a sua idade? '))

if entrada < 18:
    print('Menor de idade')
elif entrada == 18:
    print('Tem 18 anos')
else:
    print('Maior de idade')