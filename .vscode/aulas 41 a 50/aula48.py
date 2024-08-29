# tuplas
lista = [1, 2, 3]
num1, num2, num3 = lista # me obriga a ter o mesmo tamanho da lista
print(num1, num2, num3)
nome1, nome2, nome3 = ['Arthur', 'Maria', 'João'] # me obriga a ter o mesmo tamanho da lista
print(nome1, nome2, nome3)
_, _, nome3 = ['Arthur', 'Maria', 'João'] # acesso apenas ao terceiro elemento
print(nome3)
produto1, *resto = ['chinelo', 'camisa', 'sapato'] # me da liberdade de escolher o tamanho da tupla
print(produto1, resto)
prod1 = resto[0] # continuo podendo acessar os elementos da tupla
print(prod1)