from tkinter import *
from tkinter import ttk

def num_out():
    ans=[]
    n=int(num_input.get())
    for i in range(2, n + 1, 2):
        if int(str(i)[0]) <= 5 and '0' not in str(i):
            ans.append(i)

    numbers = StringVar(value=ans)
    num_list = Listbox(listvariable=numbers, background="#a6fba6", font=("Arial", 16))
    num_list.pack(side=LEFT,  fill=Y, expand=1, pady=20)
  
    scroll = ttk.Scrollbar(orient="vertical", command=num_list.yview)
    scroll.pack(side=RIGHT, fill=Y)
  
    num_list["yscrollcommand"]=scroll.set

root = Tk()
root.title("L_W_8")
root.geometry("1000x600+200+50")
root["bg"] = "#cdffcd"
root.resizable(width=False, height=False)

title = Label(text='Вывод всех четных натуральных чисел до n, при условии, что они\nне содержат нулей, а крайняя левая цифра не превышает 5.', pady=20, padx=35, font=("Times New Roman", 25), background="#007800", foreground="#ffffff")
title.pack()

input_hint = Label(text='Введите n', font=("Times New Roman", 18), background="#adff2f", padx=446)
input_hint.pack()

num_input=Entry(background="#a6fbf6")
num_input.pack(pady=25)

btn = Button(text='Запуск', font=("Times New Roman", 20), background="#ffff00", command=num_out)
btn.pack()

margin = Label(text='', background="#cdffcd")
margin.pack()

subtitle = Label(text='Числа, удовлетворяюшие условию:', font=("Times New Roman", 18), background="#adff2f", padx=316)
subtitle.pack()

root.mainloop()
