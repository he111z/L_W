class NMBRS:
    def __init__(self, n):
        self.n = n
        self.srtdnmbrs=[]

    def nmbrcrtng(self):
        for i in range(2, self.n + 1, 2):
            if int(str(i)[0]) <= 5 and '0' not in str(i):
                self.srtdnmbrs.append(i)
                
    def ans(self):
        self.nmbrcrtng()
        for i in range(len(self.srtdnmbrs)):
            print(self.srtdnmbrs[i])

print('Введите n.')
n=int(input())
print('\nВсе натуральные четные числа, не содеращие нулей, в которых 1-я цифра не превышает 5:')
crtnmbrs=NMBRS(n)
crtnmbrs.ans()
