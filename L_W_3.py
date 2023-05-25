import copy
import random

def matrix_creating(N):
    for i in range(N):
        for j in range(N):
            A[i][j]=random.randint(-10, 10)

def submatrices_creating(N):
    if N%2==0:
        B=[[A[i][j] for j in range(N//2, N)] for i in range(N//2)]
        C=[[A[i][j] for j in range(N//2, N)] for i in range(N//2, N)]
        D=[[A[i][j] for j in range(N//2)] for i in range(N//2, N)]
        E=[[A[i][j] for j in range(N//2)] for i in range(N//2)]
    if N%2==1:
        B=[[A[i][j] for j in range(N//2+1, N)] for i in range(N//2)]
        C=[[A[i][j] for j in range(N//2+1, N)] for i in range(N//2+1, N)]
        D=[[A[i][j] for j in range(N//2)] for i in range(N//2+1, N)]
        E=[[A[i][j] for j in range(N//2)] for i in range(N//2)]
    return B, C, D, E

print('С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное заполнение, а целенаправленное.')
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
print('\nКаждая из матриц B,C,D,E имеет вид:')
print('+-------+')
print('|\     /|')
print('| \ 1 / |')
print('|  \ /  |')
print('| 4 X 2 |')
print('|  / \  |')
print('| / 3 \ |')
print('|/     \|')
print('+-------+')
print('\nДля простоты все индексы в подматрицах относительные. Библиотечными методами пользоваться нельзя.')
print('\nФормируется матрица F следующим образом: если в Е количество чисел, больших К в четных столбцах в области 1 больше, чем сумма чисел в нечетных строках в области 3, то поменять в Е симметрично области 1 и 3 местами, иначе В и С поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение: A*F– K*AT (транспонированная A). Выводятся по мере формирования А, F и все матричные операции последовательно.')
N=int(input('\nВведите N:'))
K=int(input('Введите K:'))
A=[[0 for j in range(N)] for i in range(N)]#создаем матрицу...
matrix_creating(N)#...и заполняем случайними значениями
print('\nA:')
for row in A:
    print(row)#row - строка (матрицу можно рассматривать как массив строк)
F=copy.deepcopy(A)#инструмент copy.deepcopy необходим, т. к. при реализации оператора F=A оказывается, что элементы обеих матриц ссылаются на одни и те же значения. В результате при изменеии одной матрицы такие же изменения появляются и во второй
AT=copy.deepcopy(A)
B, C, D, E=submatrices_creating(N)#выделяем подматрицы
print('\nB:')
for row in B:
    print(row)
print('\nC:')
for row in C:
    print(row)
print('\nD:')
for row in D:
    print(row)
print('\nE:')
for row in E:
    print(row)
quantity_of_numbers_more_K_in_even_columns_E=0
sum_in_odd_strings_E=0
for i in range(N//2):#вычисляем количество чисел, больщих K, в четных столбцах области 1 подматрицы E...
    for j in range(N//2):
        if i+j<N//2-1 and i+j>2*i and j%2==1 and E[i][j]>K:
            quantity_of_numbers_more_K_in_even_columns_E+=1
for i in range(N//2):#...и сумму чисел в нечетных строках этой области
    for j in range(N//2):
        if i+j>N//2-1 and i+j>2*j:
            if i%2==0:
                sum_in_odd_strings_E+=E[i][j]
print('\nколичество чисел больших K в четных столбцах области "1" подматрицы E:', quantity_of_numbers_more_K_in_even_columns_E)
print('Сумма чисел в нечетных строках области "1" подматрицы E:', sum_in_odd_strings_E)
#преобразуем в зависимости от значений количества чисел и суммы
if quantity_of_numbers_more_K_in_even_columns_E>sum_in_odd_strings_E:
    for i in range(N//2):
        for j in range(N//2):
            if i+j<N//2-1 and i+j>2*i:
                temporary_storage=F[N//2-i-1][j]
                F[N//2-i-1][j]=F[i][j]
                F[i][j]=temporary_storage
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
                F[N//2+i+1][j]=temporary_storage
print('\nF:')
for row in F:
    print(row)
for i in range(N):#транспонируем
    for j in range(i, N):
        temporary_storage=AT[i][j]
        AT[i][j]=AT[j][i]
        AT[j][i]=temporary_storage
print('\nA транспонированная:')
for row in AT:
    print(row)
for i in range(N):                              #_
    for j in range(N):                          # \
        AT[i][j]*=K                             # |
R=[[0 for j in range(N)] for i in range(N)]     # |
for i in range(N):                              # \
    for j in range(N):                          #  >вычисляем итоговую матрицу
        temporary_storage=0                     # /
        for k in range(N):                      # |
            temporary_storage+=(A[i][k]*F[k][j])# |
        R[i][j]=temporary_storage-AT[i][j]      #_/
print('\nРезультат: ')
for row in R:
    print(row)
