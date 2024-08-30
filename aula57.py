# introdução a funções


def soma(x, y, z):
    print(x + y - z)


soma(2, 3, 4)  # aqui os argumentos são apenas os parametros
soma(y=8, x=5)  # aqui os argumentos são nomeados, podendo mudar a ordem
soma(
    7, z=3, y=2
)  # aqui os argumentos estão misturados entre não nomeados e nomeados, mas deve-se tomar cuidado, a partir da nomeação de um argumento, todos os que seguem ele precisam ser nomeados
