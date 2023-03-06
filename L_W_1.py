fntw={0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
text=open('text.txt')
print('Ведите "K"')
k=int(input())
print('\n')
i=0
ans=[]
while True:
    naf=True
    s1=text.readline()
    n1=''
    if s1=='':
        break
    s2=s1
    while naf==True:
        naf_in_n=True
        if s2[i].isdigit():
            n1=n1+s2[i]
            if not(s2[i+1].isdigit()):
                n2=n1
                if n2[0]=='0':
                    n2=n2.replace("0", "", 1)
                j=0
                a=int(n2)%2
                b=len(n2)%2
                if len(n2)>k:
                    c=True
                else:
                    c=False
                if a==0 and b==1 and c==True:
                    print(n2)
                    for l in range(len(n2)):
                        if not(n2[l] in ans):
                            ans.append(n2[l])
                n1=''
        if s2[i].isdigit():
            s2=s2.replace(s2[i], fntw[int(s2[i])], 1)
        i+=1
        if (not('0' in s2) and not('1' in s2) and not('2' in s2) and not('3' in s2) and not('4' in s2) and not('5' in s2) and not('6' in s2) and not('7' in s2) and not('8' in s2) and not('9' in s2)):
            naf=False
    i=0
    s1=''
for i in range(len(ans)):
    if ans[i].isdigit():
        ans[i]=ans[i].replace(ans[i], fntw[int(ans[i])], 1)
print('\n', ans, sep='')
