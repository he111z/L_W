import re
fntw={0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
text=open('text.txt')
s=''
num=[]
print('\nK=2\n')
while True:
    s=text.readline()
    if s=='':
        break
    res_s=(re.findall('[\d]*[\d]{%s}[02468]'%2, s))
    if len(res_s)>0:
        for i in range(len(res_s)):
            if len(res_s[i])%2==1:
                print(res_s[i])
                for j in range(len(res_s[i])):
                    if not((res_s[i])[j] in num):
                        num.append((res_s[i])[j])
for i in range(len(num)):
    num[i]=num[i].replace(num[i], fntw[int(num[i])], 1)
if len(num)>0:
    print('\n', num, sep='')
else:
    print('Нет чисел, удовлетворяющих условию.')
