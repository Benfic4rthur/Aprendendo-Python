# palavra_secreta = "perfume"
# monta_palavra = [
#     "_" for _ in palavra_secreta
# ]  # Cria uma lista com sublinhados para cada letra
# conta_tentativas = 0

# while "".join(monta_palavra) != palavra_secreta:  # Verifica se a palavra foi montada
#     letra = input("Digite uma letra: ")

#     if letra in palavra_secreta:
#         for i, l in enumerate(palavra_secreta):
#             if (
#                 l == letra and monta_palavra[i] == "_"
#             ):  # Substitui o sublinhado pela letra correta
#                 monta_palavra[i] = letra
#         print("Palavra atual:", "".join(monta_palavra))
#     else:
#         print("Letra não encontrada")

#     conta_tentativas += 1

# print(
#     f"Parabéns! Você acertou a palavra '{palavra_secreta}' em {conta_tentativas} tentativas."
# )
import os

palavra_secreta = "perfume"
letras_acertadas = ""
tentativas = 0

while True:

    letra_digitada = input("Digite uma letra: ")
    tentativas += 1

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra.")
        continue
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    print("Palavra formada:", palavra_formada)
    if palavra_formada == palavra_secreta:
        os.system("cls")
        print("VOCE GANHOU!!! PARABENS")
        print(f"A PALAVRA ERA: {palavra_secreta}")
        print(f"Você teve {tentativas} tentativas.")
        letras_acertadas = ""
        tentativas = 0
