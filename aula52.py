# imprecisão de numermos float
# arredondando em python
import decimal

numer01 = 0.7
numero02 = 0.1
numero03 = numero02 + numer01
print(numero03)  # imprime com incoerencia de valor
print(round(numero03, 2))  # arredonda para 2 casas
print(f"{numero03:.2f}")  # formata como uma string
print(
    decimal.Decimal.from_float(numero03)
)  # converte para decimal utilizado para numeros com muitas casas decimais

numero4 = decimal.Decimal("0.7")  # usando decimal, mas passando string
numero5 = decimal.Decimal("0.1")
numero6 = numero5 + numero4
print(numero6)
