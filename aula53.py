# split e join
frase = "olha só, que tal um split?"
lista_palavras = frase.split()  # faz a quebra de acordo com o espaço
lista_palavras_com_parametro = frase.split(
    ","
)  # faz a quebra de acordo com o parametro passado, não o espaço, o caracter passado como parametro não faz parte da lista
for i, frase in enumerate(lista_palavras_com_parametro):
    lista_palavras_com_parametro[i] = lista_palavras_com_parametro[
        i
    ].strip()  # alem do split na frase inicial é utilizado o strip para tirar os espaços em branco,
    # isso pode ser usado rstrip para remover os espaços da direita ou lstrip para remover os da esquerda

print(lista_palavras)
print(lista_palavras_com_parametro)

frases_unidas = ", ".join(
    lista_palavras_com_parametro
)  # une as strings de uma lista utilizando o join e passando o parametro de separação
print(frases_unidas)
