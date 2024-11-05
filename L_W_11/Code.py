from tkinter import *
import random 

def start_img_1_6():
    global b_1_pic_open
    global b_6_pic_open
    global count_open
    global earlier_opened
    if b_1_pic_open == True:
        btn_1['image'] = pic_0
        b_1_pic_open = False
        count_open -= 1
    if b_6_pic_open == True:
        btn_6['image'] = pic_0
        b_6_pic_open = False
        count_open -= 1
    earlier_opened = 0
def start_img_2_16():
    global b_2_pic_open
    global b_16_pic_open
    global count_open
    global earlier_opened
    if b_2_pic_open == True:
        btn_2['image'] = pic_0
        b_2_pic_open = False
        count_open -= 1
    if b_16_pic_open == True:
        btn_16['image'] = pic_0
        b_16_pic_open = False
        count_open -= 1
    earlier_opened = 0
def start_img_3_10():
    global b_3_pic_open
    global b_10_pic_open
    global count_open
    global earlier_opened
    if b_3_pic_open == True:
        btn_3['image'] = pic_0
        b_3_pic_open = False
        count_open -= 1
    if b_10_pic_open == True:
        btn_10['image'] = pic_0
        b_10_pic_open = False
        count_open -= 1
    earlier_opened = 0
def start_img_4_9():
    global b_4_pic_open
    global b_9_pic_open
    global count_open
    global earlier_opened
    if b_4_pic_open == True:
        btn_4['image'] = pic_0
        b_4_pic_open = False
        count_open -= 1
    if b_9_pic_open == True:
        btn_9['image'] = pic_0
        b_9_pic_open = False
        count_open -= 1
    earlier_opened = 0
def start_img_5_8():
    global b_5_pic_open
    global b_8_pic_open
    global count_open
    global earlier_opened
    if b_5_pic_open == True:
        btn_5['image'] = pic_0
        b_5_pic_open = False
        count_open -= 1
    if b_8_pic_open == True:
        btn_8['image'] = pic_0
        b_8_pic_open = False
        count_open -= 1
    earlier_opened = 0
def start_img_7_12():
    global b_7_pic_open
    global b_12_pic_open
    global count_open
    global earlier_opened
    if b_7_pic_open == True:
        btn_7['image'] = pic_0
        b_7_pic_open = False
        count_open -= 1
    if b_12_pic_open == True:
        btn_12['image'] = pic_0
        b_12_pic_open = False
        count_open -= 1
    earlier_opened = 0
def start_img_11_14():
    global b_11_pic_open
    global b_14_pic_open
    global count_open
    global earlier_opened
    if b_11_pic_open == True:
        btn_11['image'] = pic_0
        b_11_pic_open = False
        count_open -= 1
    if b_14_pic_open == True:
        btn_14['image'] = pic_0
        b_14_pic_open = False
        count_open -= 1
    earlier_opened = 0
def start_img_13_15():
    global b_13_pic_open
    global b_15_pic_open
    global count_open
    global earlier_opened
    if b_13_pic_open == True:
        btn_13['image'] = pic_0
        b_13_pic_open = False
        count_open -= 1
    if b_15_pic_open == True:
        btn_15['image'] = pic_0
        b_15_pic_open = False
        count_open -= 1
    earlier_opened = 0

def Button_1_pressed():
    global b_1_pic_open
    global count_open
    global earlier_opened
    global Game_started
    global is_1_6_finded
    if Game_started == False:
        Launch()
        Game_started = True
    if b_1_pic_open == False:
        btn_1['image'] = pic_3
        b_1_pic_open = True
        if earlier_opened == 0:
            earlier_opened = 1
        count_open += 1
    elif b_1_pic_open == True:
        btn_1['image'] = pic_0
        b_1_pic_open = False
        if earlier_opened == 1:
            earlier_opened = 0
        count_open -= 1
    if count_open%2 == 0:
        if earlier_opened == 6:
            Disable_1_6()
            is_1_6_finded = True
            earlier_opened = 0
            if count_open == 16:
                Victory()
        else:
            if b_1_pic_open == True:
                Disable_all()
                root.after(1000, Enable_not_found)
            root.after(1000, start_img_1_6)
            if earlier_opened == 2 or earlier_opened == 16:
                root.after(1000, start_img_2_16)
            if earlier_opened == 3 or earlier_opened == 10:
                root.after(1000, start_img_3_10)
            if earlier_opened == 4 or earlier_opened == 9:
                root.after(1000, start_img_4_9)
            if earlier_opened == 5 or earlier_opened == 8:
                root.after(1000, start_img_5_8)
            if earlier_opened == 7 or earlier_opened == 12:
                root.after(1000, start_img_7_12)
            if earlier_opened == 11 or earlier_opened == 14:
                root.after(1000, start_img_11_14)
            if earlier_opened == 13 or earlier_opened == 15:
                root.after(1000, start_img_13_15)
def Button_2_pressed():
    global b_2_pic_open
    global count_open
    global earlier_opened
    global Game_started
    global is_2_16_finded
    if Game_started == False:
        Launch()
        Game_started = True
    if b_2_pic_open == False:
        btn_2['image'] = pic_8
        b_2_pic_open = True
        if earlier_opened == 0:
            earlier_opened = 2
        count_open += 1
    elif b_2_pic_open == True:
        btn_2['image'] = pic_0
        b_2_pic_open = False
        if earlier_opened == 2:
            earlier_opened = 0
        count_open -= 1
    if count_open%2 == 0:
        if earlier_opened == 16:
            Disable_2_16()
            is_2_16_finded = True
            earlier_opened = 0
            if count_open == 16:
                Victory()
        else:
            if b_2_pic_open == True:
                Disable_all()
                root.after(1000, Enable_not_found)
            root.after(1000, start_img_2_16)
            if earlier_opened == 1 or earlier_opened == 6:
                root.after(1000, start_img_1_6)
            if earlier_opened == 3 or earlier_opened == 10:
                root.after(1000, start_img_3_10)
            if earlier_opened == 4 or earlier_opened == 9:
                root.after(1000, start_img_4_9)
            if earlier_opened == 5 or earlier_opened == 8:
                root.after(1000, start_img_5_8)
            if earlier_opened == 7 or earlier_opened == 12:
                root.after(1000, start_img_7_12)
            if earlier_opened == 11 or earlier_opened == 14:
                root.after(1000, start_img_11_14)
            if earlier_opened == 13 or earlier_opened == 15:
                root.after(1000, start_img_13_15)
def Button_3_pressed():
    global b_3_pic_open
    global count_open
    global earlier_opened
    global Game_started
    global is_3_10_finded
    if Game_started == False:
        Launch()
        Game_started = True
    if b_3_pic_open == False:
        btn_3['image'] = pic_1
        b_3_pic_open = True
        if earlier_opened == 0:
            earlier_opened = 3
        count_open += 1
    elif b_3_pic_open == True:
        btn_3['image'] = pic_0
        b_3_pic_open = False
        if earlier_opened == 3:
            earlier_opened = 0
        count_open -= 1
    if count_open%2 == 0:
        if earlier_opened == 10:
            Disable_3_10()
            is_3_10_finded = True
            earlier_opened = 0
            if count_open == 16:
                Victory()
        else:
            if b_3_pic_open == True:
                Disable_all()
                root.after(1000, Enable_not_found)
            root.after(1000, start_img_3_10)
            if earlier_opened == 1 or earlier_opened == 6:
                root.after(1000, start_img_1_6)
            if earlier_opened == 2 or earlier_opened == 16:
                root.after(1000, start_img_2_16)
            if earlier_opened == 4 or earlier_opened == 9:
                root.after(1000, start_img_4_9)
            if earlier_opened == 5 or earlier_opened == 8:
                root.after(1000, start_img_5_8)
            if earlier_opened == 7 or earlier_opened == 12:
                root.after(1000, start_img_7_12)
            if earlier_opened == 11 or earlier_opened == 14:
                root.after(1000, start_img_11_14)
            if earlier_opened == 13 or earlier_opened == 15:
                root.after(1000, start_img_13_15)
def Button_4_pressed():
    global b_4_pic_open
    global count_open
    global earlier_opened
    global Game_started
    global is_4_9_finded
    if Game_started == False:
        Launch()
        Game_started = True
    if b_4_pic_open == False:
        btn_4['image'] = pic_4
        b_4_pic_open = True
        if earlier_opened == 0:
            earlier_opened = 4
        count_open += 1
    elif b_4_pic_open == True:
        btn_4['image'] = pic_0
        b_4_pic_open = False
        if earlier_opened == 4:
            earlier_opened = 0
        count_open -= 1
    if count_open%2 == 0:
        if earlier_opened == 9:
            Disable_4_9()
            is_4_9_finded = True
            earlier_opened = 0
            if count_open == 16:
                Victory()
        else:
            if b_4_pic_open == True:
                Disable_all()
                root.after(1000, Enable_not_found)
            root.after(1000, start_img_4_9)
            if earlier_opened == 1 or earlier_opened == 6:
                root.after(1000, start_img_1_6)
            if earlier_opened == 2 or earlier_opened == 16:
                root.after(1000, start_img_2_16)
            if earlier_opened == 3 or earlier_opened == 10:
                root.after(1000, start_img_3_10)
            if earlier_opened == 5 or earlier_opened == 8:
                root.after(1000, start_img_5_8)
            if earlier_opened == 7 or earlier_opened == 12:
                root.after(1000, start_img_7_12)
            if earlier_opened == 11 or earlier_opened == 14:
                root.after(1000, start_img_11_14)
            if earlier_opened == 13 or earlier_opened == 15:
                root.after(1000, start_img_13_15)
def Button_5_pressed():
    global b_5_pic_open
    global count_open
    global earlier_opened
    global Game_started
    global is_5_8_finded
    if Game_started == False:
        Launch()
        Game_started = True
    if b_5_pic_open == False:
        btn_5['image'] = pic_6
        b_5_pic_open = True
        if earlier_opened == 0:
            earlier_opened = 5
        count_open += 1
    elif b_5_pic_open == True:
        btn_5['image'] = pic_0
        b_5_pic_open = False
        if earlier_opened == 5:
            earlier_opened = 0
        count_open -= 1
    if count_open%2 == 0:
        if earlier_opened == 8:
            Disable_5_8()
            is_5_8_finded = True
            earlier_opened = 0
            if count_open == 16:
                Victory()
        else:
            if b_5_pic_open == True:
                Disable_all()
                root.after(1000, Enable_not_found)
            root.after(1000, start_img_5_8)
            if earlier_opened == 1 or earlier_opened == 6:
                root.after(1000, start_img_1_6)
            if earlier_opened == 2 or earlier_opened == 16:
                root.after(1000, start_img_2_16)
            if earlier_opened == 3 or earlier_opened == 10:
                root.after(1000, start_img_3_10)
            if earlier_opened == 4 or earlier_opened == 9:
                root.after(1000, start_img_4_9)
            if earlier_opened == 7 or earlier_opened == 12:
                root.after(1000, start_img_7_12)
            if earlier_opened == 11 or earlier_opened == 14:
                root.after(1000, start_img_11_14)
            if earlier_opened == 13 or earlier_opened == 15:
                root.after(1000, start_img_13_15)
def Button_6_pressed():
    global b_6_pic_open
    global count_open
    global earlier_opened
    global Game_started
    global is_1_6_finded
    if Game_started == False:
        Launch()
        Game_started = True
    if b_6_pic_open == False:
        btn_6['image'] = pic_3
        b_6_pic_open = True
        if earlier_opened == 0:
            earlier_opened = 6
        count_open += 1
    elif b_6_pic_open == True:
        btn_6['image'] = pic_0
        b_6_pic_open = False
        if earlier_opened == 6:
            earlier_opened = 0
        count_open -= 1
    if count_open%2 == 0:
        if earlier_opened == 1:
            Disable_1_6()
            is_1_6_finded = True
            earlier_opened = 0
            if count_open == 16:
                Victory()
        else:
            if b_6_pic_open == True:
                Disable_all()
                root.after(1000, Enable_not_found)
            root.after(1000, start_img_1_6)
            if earlier_opened == 2 or earlier_opened == 16:
                root.after(1000, start_img_2_16)
            if earlier_opened == 3 or earlier_opened == 10:
                root.after(1000, start_img_3_10)
            if earlier_opened == 4 or earlier_opened == 9:
                root.after(1000, start_img_4_9)
            if earlier_opened == 5 or earlier_opened == 8:
                root.after(1000, start_img_5_8)
            if earlier_opened == 7 or earlier_opened == 12:
                root.after(1000, start_img_7_12)
            if earlier_opened == 11 or earlier_opened == 14:
                root.after(1000, start_img_11_14)
            if earlier_opened == 13 or earlier_opened == 15:
                root.after(1000, start_img_13_15)
def Button_7_pressed():
    global b_7_pic_open
    global count_open
    global earlier_opened
    global Game_started
    global is_7_12_finded
    if Game_started == False:
        Launch()
        Game_started = True
    if b_7_pic_open == False:
        btn_7['image'] = pic_7
        b_7_pic_open = True
        if earlier_opened == 0:
            earlier_opened = 7
        count_open += 1
    elif b_7_pic_open == True:
        btn_7['image'] = pic_0
        b_7_pic_open = False
        if earlier_opened == 7:
            earlier_opened = 0
        count_open -= 1
    if count_open%2 == 0:
        if earlier_opened == 12:
            Disable_7_12()
            is_7_12_finded = True
            earlier_opened = 0
            if count_open == 16:
                Victory()
        else:
            if b_7_pic_open == True:
                Disable_all()
                root.after(1000, Enable_not_found)
            root.after(1000, start_img_7_12)
            if earlier_opened == 1 or earlier_opened == 6:
                root.after(1000, start_img_1_6)
            if earlier_opened == 2 or earlier_opened == 16:
                root.after(1000, start_img_2_16)
            if earlier_opened == 3 or earlier_opened == 10:
                root.after(1000, start_img_3_10)
            if earlier_opened == 4 or earlier_opened == 9:
                root.after(1000, start_img_4_9)
            if earlier_opened == 5 or earlier_opened == 8:
                root.after(1000, start_img_5_8)
            if earlier_opened == 11 or earlier_opened == 14:
                root.after(1000, start_img_11_14)
            if earlier_opened == 13 or earlier_opened == 15:
                root.after(1000, start_img_13_15)
def Button_8_pressed():
    global b_8_pic_open
    global count_open
    global earlier_opened
    global Game_started
    global is_5_8_finded
    if Game_started == False:
        Launch()
        Game_started = True
    if b_8_pic_open == False:
        btn_8['image'] = pic_6
        b_8_pic_open = True
        if earlier_opened == 0:
            earlier_opened = 8
        count_open += 1
    elif b_8_pic_open == True:
        btn_8['image'] = pic_0
        b_8_pic_open = False
        if earlier_opened == 8:
            earlier_opened = 0
        count_open -= 1
    if count_open%2 == 0:
        if earlier_opened == 5:
            Disable_5_8()
            is_5_8_finded = True
            earlier_opened = 0
            if count_open == 16:
                Victory()
        else:
            if b_8_pic_open == True:
                Disable_all()
                root.after(1000, Enable_not_found)
            root.after(1000, start_img_5_8)
            if earlier_opened == 1 or earlier_opened == 6:
                root.after(1000, start_img_1_6)
            if earlier_opened == 2 or earlier_opened == 16:
                root.after(1000, start_img_2_16)
            if earlier_opened == 3 or earlier_opened == 10:
                root.after(1000, start_img_3_10)
            if earlier_opened == 4 or earlier_opened == 9:
                root.after(1000, start_img_4_9)
            if earlier_opened == 7 or earlier_opened == 12:
                root.after(1000, start_img_7_12)
            if earlier_opened == 11 or earlier_opened == 14:
                root.after(1000, start_img_11_14)
            if earlier_opened == 13 or earlier_opened == 15:
                root.after(1000, start_img_13_15)
def Button_9_pressed():
    global b_9_pic_open
    global count_open
    global earlier_opened
    global Game_started
    global is_4_9_finded
    if Game_started == False:
        Launch()
        Game_started = True
    if b_9_pic_open == False:
        btn_9['image'] = pic_4
        b_9_pic_open = True
        if earlier_opened == 0:
            earlier_opened = 9
        count_open += 1
    elif b_9_pic_open == True:
        btn_9['image'] = pic_0
        b_9_pic_open = False
        if earlier_opened == 9:
            earlier_opened = 0
        count_open -= 1
    if count_open%2 == 0:
        if earlier_opened == 4:
            Disable_4_9()
            is_4_9_finded = True
            earlier_opened = 0
            if count_open == 16:
                Victory()
        else:
            if b_9_pic_open == True:
                Disable_all()
                root.after(1000, Enable_not_found)
            root.after(1000, start_img_4_9)
            if earlier_opened == 1 or earlier_opened == 6:
                root.after(1000, start_img_1_6)
            if earlier_opened == 2 or earlier_opened == 16:
                root.after(1000, start_img_2_16)
            if earlier_opened == 3 or earlier_opened == 10:
                root.after(1000, start_img_3_10)
            if earlier_opened == 5 or earlier_opened == 8:
                root.after(1000, start_img_5_8)
            if earlier_opened == 7 or earlier_opened == 12:
                root.after(1000, start_img_7_12)
            if earlier_opened == 11 or earlier_opened == 14:
                root.after(1000, start_img_11_14)
            if earlier_opened == 13 or earlier_opened == 15:
                root.after(1000, start_img_13_15)
def Button_10_pressed():
    global b_10_pic_open
    global count_open
    global earlier_opened
    global Game_started
    global is_3_10_finded
    if Game_started == False:
        Launch()
        Game_started = True
    if b_10_pic_open == False:
        btn_10['image'] = pic_1
        b_10_pic_open = True
        if earlier_opened == 0:
            earlier_opened = 10
        count_open += 1
    elif b_10_pic_open == True:
        btn_10['image'] = pic_0
        b_10_pic_open = False
        if earlier_opened == 10:
            earlier_opened = 0
        count_open -= 1
    if count_open%2 == 0:
        if earlier_opened == 3:
            Disable_3_10()
            is_3_10_finded = True
            earlier_opened = 0
            if count_open == 16:
                Victory()
        else:
            if b_10_pic_open == True:
                Disable_all()
                root.after(1000, Enable_not_found)
            root.after(1000, start_img_3_10)
            if earlier_opened == 1 or earlier_opened == 6:
                root.after(1000, start_img_1_6)
            if earlier_opened == 2 or earlier_opened == 16:
                root.after(1000, start_img_2_16)
            if earlier_opened == 4 or earlier_opened == 9:
                root.after(1000, start_img_4_9)
            if earlier_opened == 5 or earlier_opened == 8:
                root.after(1000, start_img_5_8)
            if earlier_opened == 7 or earlier_opened == 12:
                root.after(1000, start_img_7_12)
            if earlier_opened == 11 or earlier_opened == 14:
                root.after(1000, start_img_11_14)
            if earlier_opened == 13 or earlier_opened == 15:
                root.after(1000, start_img_13_15)
def Button_11_pressed():
    global b_11_pic_open
    global count_open
    global earlier_opened
    global Game_started
    global is_11_14_finded
    if Game_started == False:
        Launch()
        Game_started = True
    if b_11_pic_open == False:
        btn_11['image'] = pic_2
        b_11_pic_open = True
        if earlier_opened == 0:
            earlier_opened = 11
        count_open += 1
    elif b_11_pic_open == True:
        btn_11['image'] = pic_0
        b_11_pic_open = False
        if earlier_opened == 11:
            earlier_opened = 0
        count_open -= 1
    if count_open%2 == 0:
        if earlier_opened == 14:
            Disable_11_14()
            is_11_14_finded = True
            earlier_opened = 0
            if count_open == 16:
                Victory()
        else:
            if b_11_pic_open == True:
                Disable_all()
                root.after(1000, Enable_not_found)
            root.after(1000, start_img_11_14)
            if earlier_opened == 1 or earlier_opened == 6:
                root.after(1000, start_img_1_6)
            if earlier_opened == 2 or earlier_opened == 16:
                root.after(1000, start_img_2_16)
            if earlier_opened == 3 or earlier_opened == 10:
                root.after(1000, start_img_11_14)
            if earlier_opened == 4 or earlier_opened == 9:
                root.after(1000, start_img_4_9)
            if earlier_opened == 5 or earlier_opened == 8:
                root.after(1000, start_img_5_8)
            if earlier_opened == 7 or earlier_opened == 12:
                root.after(1000, start_img_7_12)
            if earlier_opened == 13 or earlier_opened == 15:
                root.after(1000, start_img_13_15)
def Button_12_pressed():
    global b_12_pic_open
    global count_open
    global earlier_opened
    global Game_started
    global is_7_12_finded
    if Game_started == False:
        Launch()
        Game_started = True
    if b_12_pic_open == False:
        btn_12['image'] = pic_7
        b_12_pic_open = True
        if earlier_opened == 0:
            earlier_opened = 12
        count_open += 1
    elif b_12_pic_open == True:
        btn_12['image'] = pic_0
        b_12_pic_open = False
        if earlier_opened == 12:
            earlier_opened = 0
        count_open -= 1
    if count_open%2 == 0:
        if earlier_opened == 7:
            Disable_7_12()
            is_7_12_finded = True
            earlier_opened = 0
            if count_open == 16:
                Victory()
        else:
            if b_12_pic_open == True:
                Disable_all()
                root.after(1000, Enable_not_found)
            root.after(1000, start_img_7_12)
            if earlier_opened == 1 or earlier_opened == 6:
                root.after(1000, start_img_1_6)
            if earlier_opened == 2 or earlier_opened == 16:
                root.after(1000, start_img_2_16)
            if earlier_opened == 3 or earlier_opened == 10:
                root.after(1000, start_img_3_10)
            if earlier_opened == 4 or earlier_opened == 9:
                root.after(1000, start_img_4_9)
            if earlier_opened == 5 or earlier_opened == 8:
                root.after(1000, start_img_5_8)
            if earlier_opened == 11 or earlier_opened == 14:
                root.after(1000, start_img_11_14)
            if earlier_opened == 13 or earlier_opened == 15:
                root.after(1000, start_img_13_15)
def Button_13_pressed():
    global b_13_pic_open
    global count_open
    global earlier_opened
    global Game_started
    global is_13_15_finded
    if Game_started == False:
        Launch()
        Game_started = True
    if b_13_pic_open == False:
        btn_13['image'] = pic_5
        b_13_pic_open = True
        if earlier_opened == 0:
            earlier_opened = 13
        count_open += 1
    elif b_13_pic_open == True:
        btn_13['image'] = pic_0
        b_13_pic_open = False
        if earlier_opened == 13:
            earlier_opened = 0
        count_open -= 1
    if count_open%2 == 0:
        if earlier_opened == 15:
            Disable_13_15()
            is_13_15_finded = True
            earlier_opened = 0
            if count_open == 16:
                Victory()
        else:
            if b_13_pic_open == True:
                Disable_all()
                root.after(1000, Enable_not_found)
            root.after(1000, start_img_13_15)
            if earlier_opened == 1 or earlier_opened == 6:
                root.after(1000, start_img_1_6)
            if earlier_opened == 2 or earlier_opened == 16:
                root.after(1000, start_img_2_16)
            if earlier_opened == 3 or earlier_opened == 10:
                root.after(1000, start_img_3_10)
            if earlier_opened == 4 or earlier_opened == 9:
                root.after(1000, start_img_4_9)
            if earlier_opened == 5 or earlier_opened == 8:
                root.after(1000, start_img_5_8)
            if earlier_opened == 7 or earlier_opened == 12:
                root.after(1000, start_img_7_12)
            if earlier_opened == 11 or earlier_opened == 14:
                root.after(1000, start_img_11_14)
def Button_14_pressed():
    global b_14_pic_open
    global count_open
    global earlier_opened
    global Game_started
    global is_11_14_finded
    if Game_started == False:
        Launch()
        Game_started = True
    if b_14_pic_open == False:
        btn_14['image'] = pic_2
        b_14_pic_open = True
        if earlier_opened == 0:
            earlier_opened = 14
        count_open += 1
    elif b_14_pic_open == True:
        btn_14['image'] = pic_0
        b_14_pic_open = False
        if earlier_opened == 14:
            earlier_opened = 0
        count_open -= 1
    if count_open%2 == 0:
        if earlier_opened == 11:
            Disable_11_14()
            is_11_14_finded = True
            earlier_opened = 0
            if count_open == 16:
                Victory()
        else:
            if b_14_pic_open == True:
                Disable_all()
                root.after(1000, Enable_not_found)
            root.after(1000, start_img_11_14)
            if earlier_opened == 1 or earlier_opened == 6:
                root.after(1000, start_img_1_6)
            if earlier_opened == 2 or earlier_opened == 16:
                root.after(1000, start_img_2_16)
            if earlier_opened == 3 or earlier_opened == 10:
                root.after(1000, start_img_11_14)
            if earlier_opened == 4 or earlier_opened == 9:
                root.after(1000, start_img_4_9)
            if earlier_opened == 5 or earlier_opened == 8:
                root.after(1000, start_img_5_8)
            if earlier_opened == 7 or earlier_opened == 12:
                root.after(1000, start_img_7_12)
            if earlier_opened == 13 or earlier_opened == 15:
                root.after(1000, start_img_13_15)
def Button_15_pressed():
    global b_15_pic_open
    global count_open
    global earlier_opened
    global Game_started
    global is_13_15_finded
    if Game_started == False:
        Launch()
        Game_started = True
    if b_15_pic_open == False:
        btn_15['image'] = pic_5
        b_15_pic_open = True
        if earlier_opened == 0:
            earlier_opened = 15
        count_open += 1
    elif b_15_pic_open == True:
        btn_15['image'] = pic_0
        b_15_pic_open = False
        if earlier_opened == 15:
            earlier_opened = 0
        count_open -= 1
    if count_open%2 == 0:
        if earlier_opened == 13:
            Disable_13_15()
            is_13_15_finded = True
            earlier_opened = 0
            if count_open == 16:
                Victory()
        else:
            if b_15_pic_open == True:
                Disable_all()
                root.after(1000, Enable_not_found)
            root.after(1000, start_img_13_15)
            if earlier_opened == 1 or earlier_opened == 6:
                root.after(1000, start_img_1_6)
            if earlier_opened == 2 or earlier_opened == 16:
                root.after(1000, start_img_2_16)
            if earlier_opened == 3 or earlier_opened == 10:
                root.after(1000, start_img_3_10)
            if earlier_opened == 4 or earlier_opened == 9:
                root.after(1000, start_img_4_9)
            if earlier_opened == 5 or earlier_opened == 8:
                root.after(1000, start_img_5_8)
            if earlier_opened == 7 or earlier_opened == 12:
                root.after(1000, start_img_7_12)
            if earlier_opened == 11 or earlier_opened == 14:
                root.after(1000, start_img_11_14)
def Button_16_pressed():
    global b_16_pic_open
    global count_open
    global earlier_opened
    global Game_started
    global is_2_16_finded
    if Game_started == False:
        Launch()
        Game_started = True
    if b_16_pic_open == False:
        btn_16['image'] = pic_8
        b_16_pic_open = True
        if earlier_opened == 0:
            earlier_opened = 16
        count_open += 1
    elif b_16_pic_open == True:
        btn_16['image'] = pic_0
        b_16_pic_open = False
        if earlier_opened == 16:
            earlier_opened = 0
        count_open -= 1
    if count_open%2 == 0:
        if earlier_opened == 2:
            Disable_2_16()
            is_2_16_finded = True
            earlier_opened = 0
            if count_open == 16:
                Victory()
        else:
            if b_16_pic_open == True:
                Disable_all()
                root.after(1000, Enable_not_found)
            root.after(1000, start_img_2_16)
            if earlier_opened == 1 or earlier_opened == 6:
                root.after(1000, start_img_1_6)
            if earlier_opened == 3 or earlier_opened == 10:
                root.after(1000, start_img_3_10)
            if earlier_opened == 4 or earlier_opened == 9:
                root.after(1000, start_img_4_9)
            if earlier_opened == 5 or earlier_opened == 8:
                root.after(1000, start_img_5_8)
            if earlier_opened == 7 or earlier_opened == 12:
                root.after(1000, start_img_7_12)
            if earlier_opened == 11 or earlier_opened == 14:
                root.after(1000, start_img_11_14)
            if earlier_opened == 13 or earlier_opened == 15:
                root.after(1000, start_img_13_15)

def Digit_1_0():
    global count_open
    if count_open != 16:
        canvas.itemconfig(line_1_1, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_2, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_3, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_4, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_1_5, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_6, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_7, fill='#ee0000', outline='#000000', width=2)
def Digit_1_1():
    global count_open
    if count_open != 16:
        canvas.itemconfig(line_1_1, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_1_2, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_1_3, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_4, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_1_5, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_1_6, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_7, fill='#181818', outline='#000000', width=2)
def Digit_1_2():
    global count_open
    if count_open != 16:
        canvas.itemconfig(line_1_1, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_2, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_1_3, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_4, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_5, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_6, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_1_7, fill='#ee0000', outline='#000000', width=2)
def Digit_1_3():
    global count_open
    if count_open != 16:
        canvas.itemconfig(line_1_1, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_2, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_1_3, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_4, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_5, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_1_6, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_7, fill='#ee0000', outline='#000000', width=2)
def Digit_1_4():
    global count_open
    if count_open != 16:
        canvas.itemconfig(line_1_1, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_1_2, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_3, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_4, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_5, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_1_6, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_7, fill='#181818', outline='#000000', width=2)
def Digit_1_5():
    global count_open
    if count_open != 16:
        canvas.itemconfig(line_1_1, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_2, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_3, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_1_4, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_5, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_1_6, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_7, fill='#ee0000', outline='#000000', width=2)
def Digit_1_6():
    global count_open
    if count_open != 16:
        canvas.itemconfig(line_1_1, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_2, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_3, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_1_4, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_5, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_6, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_7, fill='#ee0000', outline='#000000', width=2)
def Digit_1_7():
    global count_open
    if count_open != 16:
        canvas.itemconfig(line_1_1, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_2, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_1_3, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_4, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_1_5, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_1_6, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_7, fill='#181818', outline='#000000', width=2)
def Digit_1_8():
    global count_open
    if count_open != 16:
        canvas.itemconfig(line_1_1, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_2, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_3, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_4, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_5, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_6, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_7, fill='#ee0000', outline='#000000', width=2)
def Digit_1_9():
    global count_open
    if count_open != 16:
        canvas.itemconfig(line_1_1, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_2, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_3, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_4, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_5, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_1_6, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_1_7, fill='#ee0000', outline='#000000', width=2)

def Digit_2_0():
    global count_open
    if count_open != 16:
        canvas.itemconfig(line_2_1, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_2, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_3, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_4, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_2_5, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_6, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_7, fill='#ee0000', outline='#000000', width=2)
def Digit_2_1():
    global count_open
    if count_open != 16:
        canvas.itemconfig(line_2_1, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_2_2, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_2_3, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_4, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_2_5, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_2_6, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_7, fill='#181818', outline='#000000', width=2)
def Digit_2_2():
    global count_open
    if count_open != 16:
        canvas.itemconfig(line_2_1, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_2, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_2_3, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_4, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_5, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_6, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_2_7, fill='#ee0000', outline='#000000', width=2)
def Digit_2_3():
    global count_open
    if count_open != 16:
        canvas.itemconfig(line_2_1, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_2, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_2_3, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_4, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_5, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_2_6, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_7, fill='#ee0000', outline='#000000', width=2)
def Digit_2_4():
    global count_open
    if count_open != 16:
        canvas.itemconfig(line_2_1, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_2_2, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_3, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_4, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_5, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_2_6, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_7, fill='#181818', outline='#000000', width=2)
def Digit_2_5():
    global count_open
    if count_open != 16:
        canvas.itemconfig(line_2_1, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_2, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_3, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_2_4, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_5, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_2_6, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_7, fill='#ee0000', outline='#000000', width=2)
def Digit_2_6():
    global count_open
    if count_open != 16:
        canvas.itemconfig(line_2_1, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_2, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_3, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_2_4, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_5, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_6, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_7, fill='#ee0000', outline='#000000', width=2)
def Digit_2_7():
    global count_open
    if count_open != 16:
        canvas.itemconfig(line_2_1, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_2, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_2_3, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_4, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_2_5, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_2_6, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_7, fill='#181818', outline='#000000', width=2)
def Digit_2_8():
    global count_open
    if count_open != 16:
        canvas.itemconfig(line_2_1, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_2, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_3, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_4, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_5, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_6, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_7, fill='#ee0000', outline='#000000', width=2)
def Digit_2_9():
    global count_open
    if count_open != 16:
        canvas.itemconfig(line_2_1, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_2, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_3, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_4, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_5, fill='#181818', outline='#000000', width=2)
        canvas.itemconfig(line_2_6, fill='#ee0000', outline='#000000', width=2)
        canvas.itemconfig(line_2_7, fill='#ee0000', outline='#000000', width=2)

def Start_1():
    global count_open
    if count_open != 16:
        canvas.itemconfig(line_1_1, fill='#181818')
        canvas.itemconfig(line_1_2, fill='#181818')
        canvas.itemconfig(line_1_3, fill='#181818')
        canvas.itemconfig(line_1_4, fill='#181818')
        canvas.itemconfig(line_1_5, fill='#181818')
        canvas.itemconfig(line_1_6, fill='#181818')
        canvas.itemconfig(line_1_7, fill='#181818')
def Start_2():
    global count_open
    if count_open != 16:
        canvas.itemconfig(line_2_1, fill='#181818')
        canvas.itemconfig(line_2_2, fill='#181818')
        canvas.itemconfig(line_2_3, fill='#181818')
        canvas.itemconfig(line_2_4, fill='#181818')
        canvas.itemconfig(line_2_5, fill='#181818')
        canvas.itemconfig(line_2_6, fill='#181818')
        canvas.itemconfig(line_2_7, fill='#181818')
        Defeat()

def Launch_1():
    root.after(0, Digit_1_8)
    root.after(1000, Digit_1_7)
    root.after(11000, Digit_1_6)
    root.after(21000, Digit_1_5)
    root.after(31000, Digit_1_4)
    root.after(41000, Digit_1_3)
    root.after(51000, Digit_1_2)
    root.after(61000, Digit_1_1)
    root.after(71000, Digit_1_0)
    root.after(72000, Start_1)
def Launch_2():
    root.after(0, Digit_2_0)
    root.after(1000, Digit_2_9)
    root.after(2000, Digit_2_8)
    root.after(3000, Digit_2_7)
    root.after(4000, Digit_2_6)
    root.after(5000, Digit_2_5)
    root.after(6000, Digit_2_4)
    root.after(7000, Digit_2_3)
    root.after(8000, Digit_2_2)
    root.after(9000, Digit_2_1)
def Launch():
    root.after(0, Launch_2)
    root.after(0, Launch_1)
    root.after(10000, Launch_2)
    root.after(20000, Launch_2)
    root.after(30000, Launch_2)
    root.after(40000, Launch_2)
    root.after(50000, Launch_2)
    root.after(60000, Launch_2)
    root.after(70000, Launch_2)
    root.after(80000, Start_2)

def Victory():
    window = Toplevel(root)
    window.title("Победа")
    window.geometry("250x60+377+406")
    icon = PhotoImage(file="App-head-image.png")
    root.iconphoto(True, icon)
    window["bg"] = "#c0ffc0"
    window.resizable(width=False, height=False)
    subtitle = Label(window, text='Вы победили!', font=("Times New Roman", 16), background="#c0ffc0", pady=85, padx=36)
    subtitle.pack()
    window.grab_set()
def Defeat():
    Disable_all()
    window = Toplevel(root)
    window.title("Поражение")
    window.geometry("250x60+377+406")
    icon = PhotoImage(file="App-head-image.png")
    root.iconphoto(True, icon)
    window["bg"] = "#ffc0c0"
    window.resizable(width=False, height=False)
    subtitle = Label(window, text='Вы проиграли!', font=("Times New Roman", 16), background="#ffc0c0", pady=85, padx=36)
    subtitle.pack()
    window.grab_set()

def Disable_1_6():
    btn_1['state'] = 'disabled'
    btn_6['state'] = 'disabled'
def Disable_2_16():
    btn_2['state'] = 'disabled'
    btn_16['state'] = 'disabled'
def Disable_3_10():
    btn_3['state'] = 'disabled'
    btn_10['state'] = 'disabled'
def Disable_4_9():
    btn_4['state'] = 'disabled'
    btn_9['state'] = 'disabled'
def Disable_5_8():
    btn_5['state'] = 'disabled'
    btn_8['state'] = 'disabled'
def Disable_7_12():
    btn_7['state'] = 'disabled'
    btn_12['state'] = 'disabled'
def Disable_11_14():
    btn_11['state'] = 'disabled'
    btn_14['state'] = 'disabled'
def Disable_13_15():
    btn_13['state'] = 'disabled'
    btn_15['state'] = 'disabled'
def Disable_all():
    btn_1['state'] = 'disabled'
    btn_2['state'] = 'disabled'
    btn_3['state'] = 'disabled'
    btn_4['state'] = 'disabled'
    btn_5['state'] = 'disabled'
    btn_6['state'] = 'disabled'
    btn_7['state'] = 'disabled'
    btn_8['state'] = 'disabled'
    btn_9['state'] = 'disabled'
    btn_10['state'] = 'disabled'
    btn_11['state'] = 'disabled'
    btn_12['state'] = 'disabled'
    btn_13['state'] = 'disabled'
    btn_14['state'] = 'disabled'
    btn_15['state'] = 'disabled'
    btn_16['state'] = 'disabled'
    
def Enable_not_found():
    global is_1_6_finded
    global is_2_16_finded
    global is_3_10_finded
    global is_4_9_finded
    global is_5_8_finded
    global is_7_12_finded
    global is_11_14_finded
    global is_13_15_finded
    if is_1_6_finded == False:
        btn_1['state'] = 'normal'
        btn_6['state'] = 'normal'
    if is_2_16_finded == False:
        btn_2['state'] = 'normal'
        btn_16['state'] = 'normal'
    if is_3_10_finded == False:
        btn_3['state'] = 'normal'
        btn_10['state'] = 'normal'
    if is_4_9_finded == False:
        btn_4['state'] = 'normal'
        btn_9['state'] = 'normal'
    if is_5_8_finded == False:
        btn_5['state'] = 'normal'
        btn_8['state'] = 'normal'
    if is_7_12_finded == False:
        btn_7['state'] = 'normal'
        btn_12['state'] = 'normal'
    if is_11_14_finded == False:
        btn_11['state'] = 'normal'
        btn_14['state'] = 'normal'
    if is_13_15_finded == False:
        btn_13['state'] = 'normal'
        btn_15['state'] = 'normal'

def How_to_play():
    window = Toplevel(root)
    window.title("Инструкция и правила")
    window.geometry("480x370+262+255")
    icon = PhotoImage(file="App-head-image.png")
    root.iconphoto(True, icon)
    window["bg"] = "#e0e0e0"
    window.resizable(width=False, height=False)
    subtitle = Label(window, text='На игровом поле 16 плиток, объединённых\nв случайные пары. Каждой паре соотверствует\nопределённое изображение.\n\nЦель игры: найти все пары изображений за\nотведённое время, в этом и заключается победа\n(после нажатия на любую плитку на табло появится\nобратный отсчёт). В случае победы на экране\nпоявится всплывающее окно с уведомлением о\nпобеде.\n\nЕсли вы не успеваете выполнить Цель за\nотведёное время, то это считается поражением (вы\nувидите всплывающее окно с соответствующим\nуведомлением).', font=("Times New Roman", 16), background="#e0e0e0", pady=85, padx=36)
    subtitle.pack()
    window.grab_set()

b_1_pic_open = False
b_2_pic_open = False
b_3_pic_open = False
b_4_pic_open = False
b_5_pic_open = False
b_6_pic_open = False
b_7_pic_open = False
b_8_pic_open = False
b_9_pic_open = False
b_10_pic_open = False
b_11_pic_open = False
b_12_pic_open = False
b_13_pic_open = False
b_14_pic_open = False
b_15_pic_open = False
b_16_pic_open = False
is_1_6_finded = False
is_2_16_finded = False
is_3_10_finded = False
is_4_9_finded = False
is_5_8_finded = False
is_7_12_finded = False
is_11_14_finded = False
is_13_15_finded = False
earlier_opened = 0
count_open = 0
move_k = random.randint(0, 7)
Game_started = False

root = Tk()
root.title("Найди пару")
icon = PhotoImage(file="App-head-image.png")
root.iconphoto(True, icon)
canvas = Canvas(root, width=600, height=540, bg="#3f3f3f")
canvas.pack()
root.geometry("600x520+200+130")
root.resizable(width=False, height=False)

canvas.create_rectangle(98, 10, 140, 81, fill="#000000")
line_1_1 = canvas.create_polygon(108, 13, 105, 16, 108, 19, 130, 19, 133, 16, 130, 13, fill="#181818")
line_1_2 = canvas.create_polygon(101, 20, 104, 17, 107, 20, 107, 42, 104, 45, 101, 42, fill="#181818")
line_1_3 = canvas.create_polygon(131, 20, 134, 17, 137, 20, 137, 42, 134, 45, 131, 42, fill="#181818")
line_1_4 = canvas.create_polygon(108, 43, 105, 46, 108, 49, 130, 49, 133, 46, 130, 43, fill="#181818")
line_1_5 = canvas.create_polygon(101, 50, 104, 47, 107, 50, 107, 72, 104, 75, 101, 72, fill="#181818")
line_1_6 = canvas.create_polygon(131, 50, 134, 47, 137, 50, 137, 72, 134, 75, 131, 72, fill="#181818")
line_1_7 = canvas.create_polygon(108, 73, 105, 76, 108, 79, 130, 79, 133, 76, 130, 73, fill="#181818")
canvas.create_rectangle(141, 10, 183, 81, fill="#000000")
line_2_1 = canvas.create_polygon(151, 13, 148, 16, 151, 19, 173, 19, 176, 16, 173, 13, fill="#181818")
line_2_2 = canvas.create_polygon(144, 20, 147, 17, 150, 20, 150, 42, 147, 45, 144, 42, fill="#181818")
line_2_3 = canvas.create_polygon(174, 20, 177, 17, 180, 20, 180, 42, 177, 45, 174, 42, fill="#181818")
line_2_4 = canvas.create_polygon(151, 43, 148, 46, 151, 49, 173, 49, 176, 46, 173, 43, fill="#181818")
line_2_5 = canvas.create_polygon(144, 50, 147, 47, 150, 50, 150, 72, 147, 75, 144, 72, fill="#181818")
line_2_6 = canvas.create_polygon(174, 50, 177, 47, 180, 50, 180, 72, 177, 75, 174, 72, fill="#181818")
line_2_7 = canvas.create_polygon(151, 73, 148, 76, 151, 79, 173, 79, 176, 76, 173, 73, fill="#181818")

photo = PhotoImage(file = 'back_img.png')
pic_0 = photo.subsample(2, 2)
photo = PhotoImage(file = 'img_' + str(move_k%8) + '.png')
pic_1 = photo.subsample(2, 2)
photo = PhotoImage(file = 'img_' + str((move_k+1)%8) + '.png')
pic_2 = photo.subsample(2, 2)
photo = PhotoImage(file = 'img_' + str((move_k+2)%8) + '.png')
pic_3 = photo.subsample(2, 2)
photo = PhotoImage(file = 'img_' + str((move_k+3)%8) + '.png')
pic_4 = photo.subsample(2, 2)
photo = PhotoImage(file = 'img_' + str((move_k+4)%8) + '.png')
pic_5 = photo.subsample(2, 2)
photo = PhotoImage(file = 'img_' + str((move_k+5)%8) + '.png')
pic_6 = photo.subsample(2, 2)
photo = PhotoImage(file = 'img_' + str((move_k+6)%8) + '.png')
pic_7 = photo.subsample(2, 2)
photo = PhotoImage(file = 'img_' + str((move_k+7)%8) + '.png')
pic_8 = photo.subsample(2, 2)

btn_HTP = Button(text = "Как играть?", font=("Times New Roman", 18), foreground = "#000000", command = How_to_play)
btn_HTP.place(x = 359, y = 22, width = 150, height = 50)
btn_1 = Button(foreground = "#000000", image = pic_0, command = Button_1_pressed)
btn_1.place(x = 98, y = 90, width = 99, height = 99)
btn_2 = Button(foreground = "#000000", image = pic_0, command = Button_2_pressed)
btn_2.place(x = 98, y = 194, width = 99, height = 99)
btn_3 = Button(foreground = "#000000", image = pic_0, command = Button_3_pressed)
btn_3.place(x = 98, y = 298, width = 99, height = 99)
btn_4 = Button(foreground = "#000000", image = pic_0, command = Button_4_pressed)
btn_4.place(x = 98, y = 402, width = 99, height = 99)
btn_5 = Button(foreground = "#000000", image = pic_0, command = Button_5_pressed)
btn_5.place(x = 202, y = 90, width = 99, height = 99)
btn_6 = Button(foreground = "#000000", image = pic_0, command = Button_6_pressed)
btn_6.place(x = 202, y = 194, width = 99, height = 99)
btn_7 = Button(foreground = "#000000", image = pic_0, command = Button_7_pressed)
btn_7.place(x = 202, y = 298, width = 99, height = 99)
btn_8 = Button(foreground = "#000000", image = pic_0, command = Button_8_pressed)
btn_8.place(x = 202, y = 402, width = 99, height = 99)
btn_9 = Button(foreground = "#000000", image = pic_0, command = Button_9_pressed)
btn_9.place(x = 306, y = 90, width = 99, height = 99)
btn_10 = Button(foreground = "#000000", image = pic_0, command = Button_10_pressed)
btn_10.place(x = 306, y = 194, width = 99, height = 99)
btn_11 = Button(foreground = "#000000", image = pic_0, command = Button_11_pressed)
btn_11.place(x = 306, y = 298, width = 99, height = 99)
btn_12 = Button(foreground = "#000000", image = pic_0, command = Button_12_pressed)
btn_12.place(x = 306, y = 402, width = 99, height = 99)
btn_13 = Button(foreground = "#000000", image = pic_0, command = Button_13_pressed)
btn_13.place(x = 410, y = 90, width = 99, height = 99)
btn_14 = Button(foreground = "#000000", image = pic_0, command = Button_14_pressed)
btn_14.place(x = 410, y = 194, width = 99, height = 99)
btn_15 = Button(foreground = "#000000", image = pic_0, command = Button_15_pressed)
btn_15.place(x = 410, y = 298, width = 99, height = 99)
btn_16 = Button(foreground = "#000000", image = pic_0, command = Button_16_pressed)
btn_16.place(x = 410, y = 402, width = 99, height = 99)

root.mainloop()
