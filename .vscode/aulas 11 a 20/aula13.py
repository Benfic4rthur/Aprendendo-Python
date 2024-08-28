nome = input("Nome: ")
altura = float(input("Altura (em metros): "))
peso = int(input("Peso (em kgs): "))
icm = peso / (altura * altura)
linha_1 = f'{nome}, seu peso é: {peso}kgs, sua altura é: {altura:.2f}m e seu ICM é: {icm:.2f}' #f-strings permite usar variáveis dentro de uma string
print(linha_1)
