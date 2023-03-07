fntw={0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
text=open('text.txt')
s=''
ans=[]
print('Введите K')
k=int(input())
while True:
    char=text.read(1)
    if char=='':
        break
    if char.isdigit():
        s=s+char
        if s[0]=='0':
            s=s.replace('0', '', 1)
    else:
        if s!='':
            if len(s)>k and len(s)%2==1 and int(s)%2==0:
                print(s)
                for i in range(len(s)):
                    if not(s[i] in ans):
                        ans.append(s[i])
            s=''
for i in range(len(ans)):
    if ans[i].isdigit():
        ans[i]=ans[i].replace(ans[i], fntw[int(ans[i])], 1)
print(ans)
