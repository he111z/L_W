def nmbrchc(n):
    for i in range(2, n + 1, 2):
        if int(str(i)[0]) <= 5 and '0' not in str(i):
            print(i)

print('Введите n.')
n=int(input())
print('\nВсе натуральные четные числа, не содеращие нулей, в которых 1-я цифра не превышает 5:')
nmbrchc(n)
