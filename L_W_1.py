print('Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом, читающимся поблочно), распознает, преобразует и выводит на экран числа по определенному правилу. Числа распознаются по законам грамматики русского языка. Преобразование делать по возможности через словарь. Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа. Регулярные выражения использовать нельзя.\n')
print('Натуральные числа. Выводит на экран четные числа, содержащие нечетное количество цифр, превышающее К.\nСписок используемых цифр выводится отдельно прописью.\n')
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
                j=0
                a=int(n2)%2
                b=len(n2)%2
                if int(n2)>k:
                    c=True
                else:
                    c=False
                if a==0 and b==1 and c==True:
                    print(int(n2))
                while naf_in_n==True:
                    if n2[j].isdigit():
                        n2=n2.replace(n2[j], fntw[int(n2[j])]+' ', 1)
                    j+=1
                    if (not('0' in n2) and not('1' in n2) and not('2' in n2) and not('3' in n2) and not('4' in n2) and not('5' in n2) and not('6' in n2) and not('7' in n2) and not('8' in n2) and not('9' in n2)):
                        naf_in_n=False
                if a==0 and b==1 and c==True:
                    ans.append(n2)
                n1=''
        if s2[i].isdigit():
            s2=s2.replace(s2[i], fntw[int(s2[i])], 1)
        i+=1
        if (not('0' in s2) and not('1' in s2) and not('2' in s2) and not('3' in s2) and not('4' in s2) and not('5' in s2) and not('6' in s2) and not('7' in s2) and not('8' in s2) and not('9' in s2)):
            naf=False
    i=0
    s1=''
print('\n', ans, sep='')
