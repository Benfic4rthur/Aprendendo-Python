# if / elif       / else
# se / se não se / se não

# entrada = int(input('Qual a sua idade? '))

# if entrada < 18:
#     print('Menor de idade')
# elif entrada == 18:
#     print('Tem 18 anos')
# else:
#     print('Maior de idade')

nome = input('Qual o seu nome? ')
nota1 = int(input('Qual foi sua primeira nota? '))
nota2 = int(input('Qual foi sua segunda nota? '))
nota3 = int(input('Qual foi sua terceira nota? '))
media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f'{nome}, sua média foi {media}, parabéns e voce foi aprovado!')
elif media >= 5:
    print(f'{nome}, sua média foi {media}, você ficou em recuperação!')
else:
    print(f'{nome}, sua média foi {media}, você foi reprovado!')