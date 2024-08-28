frase = "Estou aprendendo Python para um projeto da DMSYS"
i = 0
qtd_vezes_que_aparece = 0
letra_que_apareceu_mais_vezes = ""

while i < len(frase):
    letra_atual = frase[i]
    qtd_vezes_que_aparece_atual = frase.count(letra_atual)

    if qtd_vezes_que_aparece < qtd_vezes_que_aparece_atual and letra_atual != " ":
        qtd_vezes_que_aparece = qtd_vezes_que_aparece_atual
        letra_que_apareceu_mais_vezes = letra_atual.upper()

    i += 1

print(f"A letra que apareceu mais vezes foi: {letra_que_apareceu_mais_vezes}")
print(
    f"A letra '{letra_que_apareceu_mais_vezes}' apareceu {qtd_vezes_que_aparece} vezes"
)
