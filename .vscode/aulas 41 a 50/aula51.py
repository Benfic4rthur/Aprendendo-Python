import os

lista = []

while True:
    print("Selecione uma opção")
    opcao = input("[i]nseririr [a]pagar [l]istar: ").lower()

    if opcao == "i":
        os.system("cls")
        incluir = input("Nome: ").lower()
        lista.append(incluir)
        os.system("cls")
    elif opcao == "a":
        if len(lista) == 0:
            os.system("cls")
            print("Nada para apagar")
        else:
            os.system("cls")
            apagar = input("Nome: ").lower()
            if apagar in lista:
                os.system("cls")
                lista.remove(apagar)
            else:
                print("Nome não encontrado")
    elif opcao == "l":
        if len(lista) == 0:
            os.system("cls")
            print("Nada para listar")
        else:
            os.system("cls")
            print(*lista, sep="-")
    else:
        print("Opção inválida")
