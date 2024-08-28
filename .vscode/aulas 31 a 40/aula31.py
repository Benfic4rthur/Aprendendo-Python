hora = input("Digite que horas são(24hrs): ")
if int(hora) > 0 and int(hora) < 12:
    print("Bom dia")
elif int(hora) > 12 and int(hora) < 18:
    print("Boa tarde")
else:
    print("Boa noite")
