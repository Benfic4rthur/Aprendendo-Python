#interpolação basica
nome = 'Arthur'
preco = 19.99
# variavel = f'{nome} o preço e {preco:.2f}'
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)