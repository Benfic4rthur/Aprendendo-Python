# enumarate list
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_enumerada = enumerate(lista)
lista_enumerada_tipada = list(
    enumerate(lista, start=1)
)  # consigo definir o start do indice
lista_nomes = ["João", "Maria", "Pedro", "Ana"]
print(lista)  # imprime a lista apenas
print(lista_enumerada)  # imprime um iterador
print(lista_enumerada_tipada)  # imprime uma lista com indices

for nomes in list(enumerate(lista_nomes, start=1)):
    print(nomes)

for indices, nomes in enumerate(lista_nomes, start=1):
    print(indices, nomes)
