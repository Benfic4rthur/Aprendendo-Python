def soma(x, y, z=None):
    if z is not None:
        print(f"{x=} {y=} {z=}", x + y + z)
    else:
        print(f"{x=} {y=}", x + y)


soma(2, 3)
soma(2, 3, 4)
soma(2, 3, None)
