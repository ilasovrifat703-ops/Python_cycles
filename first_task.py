x_st = int(input())
x_end = int(input())
dx = float(input())

while x_st <= x_end:
    x_st+=dx
    if x_st <= (-6):
        print(f'Значение x: {x_st}, Значение y: 2')
    elif x_st <= (-2):
        print(f'Значение x: {x_st}, Значение y: {x_st*0.25 + 0.5}')
    elif x_st <= 0:
        print(f'Значение x: {x_st}, Значение y: {round(2 - ((4 - (x_st+2)**2)**0.5),2)}')
    elif x_st <= 2:
        print(f'Значение x: {x_st}, Значение y: {round((4-x_st**2)**0.5,2)}')
    else:
        print(f'Значение x: {x_st}, Значение y: {2 - x_st}')