nome = input("Nome: ")
altura = input("altura: ")
peso = input("Peso:")
icm = int(peso) / (float(altura) * float(altura))
print("Arthur, seu peso é:", peso, "kgs, sua altura é:", altura, "m e seu ICM é:", icm)