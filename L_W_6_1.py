print('Введите n.')
n=int(input())
print('\nВсе натуральные четные числа, в которых 1-я цифра не превышает 5:')
for i in range(2, n+1, 2):
    if int(str(i)[0]) <= 5:
        print(i)
