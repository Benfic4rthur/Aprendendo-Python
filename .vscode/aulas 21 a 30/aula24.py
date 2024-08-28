# fatiamento de strings
string = 'arthur'
print(string[0]) # acesso o indice determinado
print(string[2:]) # começa a fatiar a string do indice determinado, vai passar tudo depois do indice 2
print(string[2:4]) # passa o indice inicial e final para fatiar, caso queira um valor determinado sempre lançar um a mais no final
print(string[2:5]) # passa o indice inicial e final para fatiar, caso queira um valor determinado sempre adicionar um a mais no final
print(len(string)) # tamanho da string
print(string[0:6:1]) # inicio:tamanho:passo
print(string[0:6:2]) # inicio:tamanho:passo
print(string[::-1]) # inverte a string  