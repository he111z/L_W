import copy
import random
import numpy as np
import matplotlib.pyplot as plt

def matrix_creating(N):
    for i in range(N):
        for j in range(N):
            A[i][j] = random.randint(-10, 10)

def submatrices_creating(N):
    if N % 2 == 0:
        B = [[A[i][j] for j in range(N // 2, N)] for i in range(N // 2)]
        C = [[A[i][j] for j in range(N // 2, N)] for i in range(N // 2, N)]
        D = [[A[i][j] for j in range(N // 2)] for i in range(N // 2, N)]
        E = [[A[i][j] for j in range(N // 2)] for i in range(N // 2)]
    if N % 2 == 1:
        B = [[A[i][j] for j in range(N // 2 + 1, N)] for i in range(N // 2)]
        C = [[A[i][j] for j in range(N // 2 + 1, N)] for i in range(N // 2 + 1, N)]
        D = [[A[i][j] for j in range(N // 2)] for i in range(N // 2 + 1, N)]
        E = [[A[i][j] for j in range(N // 2)] for i in range(N // 2)]
    return B, C, D, E

print('С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10]. Для отладки использовать не случайное заполнение, а целенаправленное.')
print('\nВид матрицы А:')
print('+---|---+')
print('|   |   |')
print('| E | B |')
print('|   |   |')
print('+---+---+')
print('|   |   |')
print('| D | C |')
print('|   |   |')
print('+---+---+')
print('Для простоты все индексы в подматрицах относительные.')
print('Формируется матрица F следующим образом: скопировать в нее А и  если в Е количество чисел, больших К в четных столбцах больше, чем сумма чисел в нечетных строках, то поменять местами С и Е симметрично, иначе В и С поменять местами несимметрично. При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F, то вычисляется выражение: A * AT – K * FТ, иначе вычисляется выражение (AТ + G обр. - F обр.) * K, где G-нижняя треугольная матрица, полученная из А. Выводятся по мере формирования А, F и все матричные операции последовательно.')
print('По сформированной матрице F (или ее частям) необходимо вывести не менее 3 разных графиков.')
print('Программа должна использовать функции библиотек numpy  и mathplotlib')

N=int(input('\nВведите N: '))
K=int(input('Введите K: '))
A=[[0 for j in range(N)] for i in range(N)]
matrix_creating(N)
print('\nA:')
for row in A:
    print(row)
B, C, D, E=submatrices_creating(N)
print('\nE:')
for row in E:
    print(row)
print('\nB:')
for row in B:
    print(row)
print('\nD:')
for row in D:
    print(row)
print('\nC:')
for row in C:
    print(row)
F=copy.deepcopy(A)
AT=copy.deepcopy(A)
FT=copy.deepcopy(A)
G=copy.deepcopy(A)
R=copy.deepcopy(A)
quantity_of_numbers_more_K_in_even_columns_E=0
sum_in_odd_strings_E=0
for i in range(N//2):
    for j in range(N//2):
        if j%2==1 and E[i][j]>K:
            quantity_of_numbers_more_K_in_even_columns_E+=1
for i in range(N//2):
    for j in range(N//2):
        if i%2==0:
            sum_in_odd_strings_E+=E[i][j]
print('\nКоличество чисел больших K в четных столбцах подматрицы E:', quantity_of_numbers_more_K_in_even_columns_E)
print('Сумма чисел в нечетных строках подматрицы E:', sum_in_odd_strings_E)
if quantity_of_numbers_more_K_in_even_columns_E>sum_in_odd_strings_E:
    for i in range(N//2):
        for j in range(N//2, N):
            temporary_storage=F[i][j]
            F[i][j]=F[N-1-i][j]
            F[N-1-i][j]=temporary_storage
else:
    if N%2==0:
        for i in range(N//2):
            for j in range(N//2, N):
                temporary_storage=F[i][j]
                F[i][j]=F[N//2+i][j]
                F[N//2+i][j]=temporary_storage
    if N%2==1:
        for i in range(N//2):
            for j in range(N//2+1, N):
                temporary_storage=F[i][j]
                F[i][j]=F[N//2+i+1][j]
                F[N//2+i+1][j] = temporary_storage
print('\nF:')
for row in F:
    print(row)
det_A=np.linalg.det(A)
if det_A-int(det_A)>=0.5:
    det_A=(int(det_A)+1)
else:
    det_A=(int(det_A))
print('\nОпределитель матрицы A', det_A)
sum_diag_F=0
for i in range(N):
    for j in range(N):
        if i==j or (i==N-j-1):
            sum_diag_F+=F[i][j]
print('Сумма диагональных элементов F:', sum_diag_F)
if det_A>sum_diag_F:
    AT=np.transpose(A)
    print('\nAT:')
    for row in AT:
        print(row)
    FT=np.transpose(F)
    print('\nFT:')
    for row in FT:
        print(row)
    reduced=np.matmul(A,AT)
    for i in range(N):
        for j in range(N):
            R[i][j]=reduced[i][j]-K*FT[i][j]
    print('\nРезультат:')
    for row in R:
        print(row)
else:
    G=np.tril(A, k=0)
    Inv_G=copy.deepcopy(G)
    print('\nG:')
    for row in G:
        print(row)
    det_G=np.linalg.det(G)
    if det_G-int(det_G)>=0.5:
        det_G=(int(det_G)+1)
    else:
        det_G=(int(det_G))
    det_F=np.linalg.det(F)
    if det_F-int(det_F)>=0.5:
        det_F=(int(det_F)+1)
    else:
        det_F=(int(det_F))
    if det_G!=0:
        Inv_G=np.linalg.inv(G)
        if det_F!=0:
            Inv_F=np.linalg.inv(F)
            for i in range(N):
                for j in range(N):
                    R[i][j]=(AT[i][j]+Inv_G[i][j]-Inv_F[i][j])*K
            print('\nРезультат:')
            for row in R:
                print(row)
        else:
            print('Det(F)=0 - невозможно инвертировать F')
            R=0
    else:
        print('Det(G)=0 - невозможно инвертировать G')
        R=0

plt.figure(figsize=(6, 4))
plt.imshow(A, cmap='coolwarm')
plt.title('A')
plt.colorbar()
plt.show()

plt.figure(figsize=(6, 4))
plt.imshow(F, cmap='coolwarm')
plt.title('F')
plt.colorbar()
plt.show()

if R!=0:
    plt.figure(figsize=(6, 4))
    plt.imshow(R, cmap='coolwarm')
    plt.title('Результат')
    plt.colorbar()
    plt.show()
