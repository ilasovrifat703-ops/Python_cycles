def find_sum(num):
    result = []
    for i in str(num):
        result.append(int(i)**2)
    return sum(result)

for i in range(10,100):
    if find_sum(i) % 10 == 0:
        print(i)
