# flag = marcar local
# None = não valor
# is e is not = é ou não é
# id = identificador de variavel

condicao = True
passounoif = None
if condicao:
    passounoif = True
    print("verdadeiro")
else:
    print("falso")
print(passounoif, passounoif is None)  # checa se a variavel passounoif e None
print(passounoif, passounoif is not None)  # checa se a variavel passounoif não e None

if passounoif is None:
    print("Não passou no if")
else:
    print("Passou no if")
