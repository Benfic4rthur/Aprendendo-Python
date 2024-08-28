while True:
    try:
        numero_1 = int(input("Digite um número: "))
        numero_2 = int(input("Digite outro número: "))
    except ValueError:
        print("Um ou ambos os operandos são inválidos")
        continue

    operador = input("Digite um operador (+, -, *, /): ")

    if operador == "+":
        print(f"Resultado: {numero_1 + numero_2}")
    elif operador == "-":
        print(f"Resultado: {numero_1 - numero_2}")
    elif operador == "*":
        print(f"Resultado: {numero_1 * numero_2}")
    elif operador == "/":
        if numero_2 == 0:
            print("Erro: Divisão por zero não é permitida.")
        else:
            print(f"Resultado: {numero_1 / numero_2}")
    else:
        print("Operador inválido")

    continuar = input("Deseja continuar? [s/n] ").lower().startswith("s")

    if not continuar:
        break

print("Encerrando a calculadora.")
