x = [14,21,45,63,11,12,14,87]

for i in range(len(x)):
    num1 = x[i]
    for j in range(len(x)):
        product = num1 * x[j]
        if product % 2 != 0:
            print(num1 , x[j])
