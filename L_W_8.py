from tkinter import *
from tkinter import ttk

def num_out():
    window = Tk()
    window.title("Результат")
    window.geometry("400x300+250+300")
    window["bg"] = "#dffaff"
    window.resizable(width=False, height=False)
    n=(num_input.get())
    if n != "":
        if n.isnumeric():
            subtitle = Label(window, text='Числа, удовлетворяюшие условию:', font=("Times New Roman", 18), background="#81d5f5", pady=5, padx=17)
            subtitle.pack()
            n=int(n)
            ans=[]
            for i in range(2, n + 1, 2):
                if int(str(i)[0]) <= 5 and '0' not in str(i):
                    ans.append(i)
            numbers = StringVar(window, value=ans)
            num_list = Listbox(window, listvariable=numbers, background="#a6fbf6", font=("Arial", 16))
            num_list.pack(side=LEFT,  fill=Y, expand=2, pady=20)
            scroll = ttk.Scrollbar(window, orient="vertical", command=num_list.yview)
            scroll.pack(side=RIGHT, fill=Y)
            num_list["yscrollcommand"]=scroll.set
        else:
            window.title("ERROR!!!")
            window["bg"] = "#ff0000"
            subtitle = Label(window, text='ERROR!\nВвод содержит\nне только цифры!', font=("Times New Roman", 24), background="#ff0000", foreground="#ffff00", pady=85, padx=76)
            subtitle.pack()
    else:
        window.title("ERROR!!!")
        window["bg"] = "#ff0000"
        subtitle = Label(window, text='ERROR!\nЧисло не введено!', font=("Times New Roman", 24), background="#ff0000", foreground="#ffff00", pady=100, padx=73)
        subtitle.pack()
root = Tk()
root.title("L_W_8")
root.geometry("700x360+300+150")
root["bg"] = "#dffaff"
root.resizable(width=False, height=False)
title = Label(text='Вывод всех четных натуральных чисел до n,\nпри условии, что они не содержат нулей, а\nкрайняя левая цифра не превышает 5.', pady=20, padx=38, font=("Times New Roman", 25), background="#81d5f5", foreground="#000000")
title.pack()
input_hint = Label(text='Введите n', font=("Times New Roman", 18), background="#dffaff", padx=446, pady=20)
input_hint.pack()
num_input=Entry(background="#a6fbf6")
num_input.pack(pady=0)
btn = Button(text='Запуск', font=("Times New Roman", 24), background="#3ab0ff", foreground="#ffff00", command=num_out)
btn.pack(pady=25)
margin = Label(text='', background="#cdffcd")
margin.pack()
root.mainloop()
