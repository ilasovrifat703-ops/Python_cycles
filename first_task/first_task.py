x_st = int(input())
x_end = int(input())
dx = float(input())

print('x   |   y')
while x_st <= x_end:
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
    else:
        y = round(2 - x_st, 2)
        print(f'{round(x_st, 2)} {y}')

    x_st += dx
