x_st = int(input())
x_end = int(input())
dx = float(input())

print('x   |   y')
while x_st <= x_end:
<<<<<<< HEAD
    if x_st <= -6:
        y = 2
        print(f'{round(x_st, 2)} {y}')
    elif x_st <= -2:
        y = round(x_st * 0.25 + 0.5, 2)
        print(f'{round(x_st, 2)} {y}')
    elif x_st <= 0:
        y = round(2 - ((4 - (x_st + 2)**2)**0.5), 2)
        print(f'{round(x_st, 2)} {y}')
    elif x_st <= 2:
        y = round((4 - x_st**2)**0.5, 2)
        print(f'{round(x_st, 2)} {y}')
=======
    x_st += dx
    if x_st <= (-6):
        print(f'Значение x: {x_st}, Значение y: 2')
    elif x_st <= (-2):
        print(f'Значение x: {x_st}, Значение y: {x_st * 0.25 + 0.5}')
    elif x_st <= 0:
        print(f'Значение x: {x_st}, Значение y: {round(2 - ((4 - (x_st + 2)**2)**0.5), 2)}')
    elif x_st <= 2:
        print(f'Значение x: {x_st}, Значение y: {round((4 - x_st**2)**0.5, 2)}')
>>>>>>> bf1741e4732749a4f2e200cf36d25011b740d4e9
    else:
        y = round(2 - x_st, 2)
        print(f'{round(x_st, 2)} {y}')

    x_st += dx
