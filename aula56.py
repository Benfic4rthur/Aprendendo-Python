import os

while True:
    cpf = input("digite seu cpf: ")
    if len(cpf) != 11:
        os.system("cls")
        print("Quantidade de digitos invalida")
        continue
    elif len(cpf) == 11 and not cpf.isnumeric():
        os.system("cls")
        print("Quantidade de digitos invalida ou letras digitadas")
        continue
    nove_digitos = cpf[:9]
    contador_regressivo_1 = 10
    contador_regressivo_2 = 11
    resultado_digito_1 = 0
    resultado_digito_2 = 0
    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0
    dez_digitos = nove_digitos + str(digito_1)
    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0
    if digito_1 == int(cpf[9]) and digito_2 == int(cpf[10]):
        os.system("cls")
        print(f"O CPF {cpf} informado e valido")
    else:
        os.system("cls")
        print(f"O CPF {cpf} informado e invalido")
