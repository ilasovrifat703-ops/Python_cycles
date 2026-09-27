for num in range(10, 100):
    sum_digits = (num % 10)**2 + (num // 10)**2
    if sum_digits % 10 == 0:
        print(num)
