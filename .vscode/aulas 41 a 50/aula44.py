# metodos uteis na lista
# append, insert, pop, del, clear, extend, +
lista = [10, 20, 30, 40, 50]  # lista original
print(lista)  # mostra a lista
lista.append(60)  # adiciona na ultima posicao
print(lista)  # mostra a lista com o elemento adicionado
ultimo_valor = (
    lista.pop()
)  # remove o elemento da posição escolhida, caso não escolhe remove da ultima posicao, o pop tambem salva o valor removidoem uma variavel
print(
    lista, " ultimo valor removido: ", ultimo_valor
)  # mostra a lista com o elemento removido
lista.insert(2, 25)  # insere na posicao 2 o valor 25
print(lista)  # mostra a lista com o elemento inserido
lista.clear()  # limpa a lista
print(lista)  # mostra a lista limpa
lista_2 = [1, 2, 3]
lista.extend(lista_2)  # adiciona os elementos da lista_2 na lista
print(lista)  # mostra a lista com os elementos da lista_2 adicionados
soma = sum(lista)  # soma os elementos da lista
print(soma)  # mostra a soma dos elementos
lista_3 = lista + lista_2
print(lista_3)  # mostra a lista concatenada
