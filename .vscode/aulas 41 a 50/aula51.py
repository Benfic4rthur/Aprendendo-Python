import os

lista = []

while True:
    print("Selecione uma opção")
    opcao = input("[i]nserir [a]pagar [l]istar: ").lower()

    if opcao == "i":
        os.system("cls")
        incluir = input("Nome: ").lower()
        lista.append(incluir)
        os.system("cls")

    elif opcao == "a":
        os.system("cls")
        if not lista:
            print("Nada para apagar")
        else:
            apagar = input("Nome: ").lower()
            if apagar in lista:
                lista.remove(apagar)
                print(f"Nome '{apagar}' removido com sucesso.")
            else:
                print("Nome não encontrado")

    elif opcao == "l":
        os.system("cls")
        if not lista:
            print("Nada para listar")
        else:
            print("Lista de nomes:", *lista, sep=" - ")

    else:
        print("Opção inválida")
