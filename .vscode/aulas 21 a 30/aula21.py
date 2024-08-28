# # operador in e not in
# nome = 'arthur'
# print(nome[0])
# print('a' in nome)
# print('a' not in nome)
nome = input('Nome: ')
encontrar = input('Encontrar: ')

if encontrar in nome:
    print(f'Encontrado {encontrar} no nome {nome}')
else:
    print(f'Não encontrado {encontrar} no nome {nome}')