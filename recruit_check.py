import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np


def import_data(txt):
    file=open('{}'.format(txt),'r',encoding='UTF-8')
    lines=file.readlines()
    file.close()
    return lines

def check_data(lines):
    temp_recruit=[]
    for i in range(len((lines))):
        lines[i]=lines[i].strip().split('\t')
        if len(lines[i])==4:
            lines[i]+=['연봉정보없음!']
        elif len(lines[i])==5:
            pay=''
            for m in range(len(lines[i][4])):
                if lines[i][4][m].isdigit():
                    pay+=lines[i][4][m]
            lines[i][4]=pay
            if len(lines[i][4])==3:
                lines[i][4]=str(int(lines[i][4])*12)
            elif len(lines[i][4])==5:
                lines[i][4] = str(int(int(lines[i][4]) * 209 * 12 / 10000))
    for i in range(len(lines)):
        if len(lines[i])!=5:
            pass
        else:
            temp_recruit.append(lines[i])
    return temp_recruit

# 도시 추출
def check_city(temp_recruit):
    city_n = []
    for i in range(len(temp_recruit)):
        temp_recruit[i][0] = temp_recruit[i][0].split(' ')[0]
        if '전체' in temp_recruit[i][0]:
            temp_recruit[i][0] = temp_recruit[i][0].replace('전체', '')
        if temp_recruit[i][0] not in city_n:
            city_n.append(temp_recruit[i][0])

    return city_n

# 연봉 추출
def check_pay(temp_recruit):
    c_pay = []

    for i in range(len(temp_recruit)):
        if temp_recruit[i][4] not in c_pay:
            c_pay.append(temp_recruit[i][4])

    return c_pay

# 학력 추출
def check_edu(temp_recruit):
    c_edu = []

    for i in range(len(temp_recruit)):
        if temp_recruit[i][2] not in c_edu:
            c_edu.append(temp_recruit[i][2])

    return c_edu

# 정규직
def check_sta(temp_recruit):
    c_sta = []

    for i in range(len(temp_recruit)):
        if '정규직' in temp_recruit[i][3]:
            temp_recruit[i][3] = '정규직'
        elif '계약직' in temp_recruit[i][3]:
            temp_recruit[i][3] = '계약직'
        elif '병역특례' in temp_recruit[i][3]:
            temp_recruit[i][3]='병역특례'
        elif '아르바이트' in temp_recruit[i][3]:
            temp_recruit[i][3]='아르바이트'
        elif '프리랜서' in temp_recruit[i][3]:
            temp_recruit[i][3]='프리랜서'
        elif '산업기능요원' in temp_recruit[i][3]:
            temp_recruit[i][3]='산업기능요원'
        if temp_recruit[i][3] not in c_sta:
            c_sta.append(temp_recruit[i][3])

    return c_sta

# 신입 or 경력
def check_y(temp_recruit):
    c_y = []

    for i in range(len(temp_recruit)):
        if '신입' in temp_recruit[i][1] or '경력무관' in temp_recruit[i][1]:
            temp_recruit[i][1]='신입'
        elif '경력' in temp_recruit[i][1]:
            temp_recruit[i][1]='경력'
        if temp_recruit[i][1] not in c_y:
            c_y.append(temp_recruit[i][1])

    return c_y

def move_toFrame2():
    global check_1
    check_1=[]
    for i in range(len(city_n)):
        check_1.append(globals()['CheckVar{}'.format(i)].get())
    print(check_1)
    frame_2.tkraise()

def move_toFrame3():
    global check_2
    check_2=entry_2_1.get()
    if check_2.isdigit():
        frame_3.tkraise()
    print(check_2)

def move_toFrame4():
    global check_3
    check_3=[]
    for i in range(len(c_edu)):
        check_3.append(globals()['e_CheckVar{}'.format(i)].get())
    print(check_3)
    frame_4.tkraise()

def move_toFrame5():
    global check_4
    check_4=[]
    for i in range(len(c_sta)):
        check_4.append(globals()['s_CheckVar{}'.format(i)].get())
    print(check_4)
    frame_5.tkraise()

def move_toFrame6():
    global check_1
    global city_n

    global check_2
    global c_pay

    global check_3
    global c_edu

    global check_4
    global c_sta

    global check_5
    global c_y

    global temp_recruit

    global last_temp5

    check_5=[]
    for i in range(len(c_y)):
        check_5.append(globals()['y_CheckVar{}'.format(i)].get())
    print('경력',check_5)

    last_temp=[]
    for i in range(len(city_n)):
        if check_1[i] == 0:
            pass
        else:
            for m in range(len(temp_recruit)):
                if city_n[i] in temp_recruit[m][0]:
                    last_temp.append(temp_recruit[m])

    last_temp2=[]
    if check_2 == '0':
        for i in range(len(last_temp)):
            last_temp2.append(last_temp[i])
    else:
        for i in range(len(last_temp)):
            if last_temp[i][4] == '연봉정보없음!':
                pass
            elif int(last_temp[i][4]) >= int(check_2):
                last_temp2.append(last_temp[i])

    last_temp3=[]
    for i in range(len(c_edu)):
        if check_3[i] == 0:
            pass
        else:
            for m in range(len(last_temp2)):
                if c_edu[i] in last_temp2[m][2]:
                    last_temp3.append(last_temp2[m])

    last_temp4=[]
    for i in range(len(c_sta)):
        if check_4[i] == 0:
            pass
        else:
            for m in range(len(last_temp3)):
                if c_sta[i] in last_temp3[m][3]:
                    last_temp4.append(last_temp3[m])

    last_temp5=[]
    for i in range(len(c_y)):
        if check_5[i] == 0:
            pass
        else:
            for m in range(len(last_temp4)):
                if c_y[i] in last_temp4[m][1]:
                    last_temp5.append(last_temp4[m])



    plt.rcParams['font.family'] = 'Malgun Gothic'
    cat = []
    values = []

    for i in range(len(last_temp5)):
        if last_temp5[i][0] not in cat:
            cat.append(last_temp5[i][0])
            values.append(1)
            print(cat)
            print(values)
        else:
            values[cat.index(last_temp5[i][0])]+=1
            print(values)

    x = np.arange(len(cat))
    plt.bar(x, values)
    plt.xticks(x, cat)
    plt.title('채용정보', loc='right', pad=20)
    plt.xlabel('지역', labelpad=10)
    plt.ylabel('건 수', labelpad=8)
    y = sorted(values)[-1]
    x_2 = len(cat)
    for i, v in enumerate(x):
        plt.text(v, values[i], values[i],  # 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
                 fontsize=9,
                 color='blue',
                 horizontalalignment='center',  # horizontalalignment (left, center, right)
                 verticalalignment='bottom')  # verticalalignment (top, center, bottom)

    plt.ylim([0, (y+130)])
    plt.show()


    return last_temp5

def check_all():
    for i in range(len(city_n)):
        globals()['c{}'.format(i)].toggle()

def check_all2():
    for i in range(len(c_edu)):
        globals()['e{}'.format(i)].toggle()

def check_all3():
    for i in range(len(c_sta)):
        globals()['s{}'.format(i)].toggle()

def check_all4():
    for i in range(len(c_y)):
        globals()['y{}'.format(i)].toggle()

if __name__=='__main__':
    lines = import_data('채용 데이터.txt')
    temp_recruit = check_data(lines)
    city_n = check_city(temp_recruit)
    c_pay = check_pay(temp_recruit)
    c_edu=check_edu(temp_recruit)
    c_sta=check_sta(temp_recruit)
    c_y=check_y(temp_recruit)

    window=tk.Tk()
    window.geometry('400x600')
    window.resizable(False,False)


    frame_2=tk.Frame(window)
    frame_2.place(x=0, y=0, width=400, height=600)
    label_2_1=tk.Label(frame_2,text='희망연봉 기입. \n상관없으면 0')
    label_2_1.pack()
    entry_2_1=tk.Entry(frame_2)
    entry_2_1.pack()
    button_2_1=tk.Button(frame_2,text='확인',command=move_toFrame3)
    button_2_1.pack()

    frame_3=tk.Frame(window)
    frame_3.place(x=0, y=0, width=400, height=600)
    for i in range(len(c_edu)):
        globals()['e_CheckVar{}'.format(i)] = tk.IntVar()
        globals()['e{}'.format(i)] = tk.Checkbutton(frame_3, text="{}".format(c_edu[i]),
                                                    variable=eval('e_CheckVar{}'.format(i)))
        globals()['e{}'.format(i)].pack()
    button_3_1=tk.Button(frame_3,text='확인',command=move_toFrame4)
    button_3_1.pack()
    button_3_2=tk.Button(frame_3,text='모두 선택',command=check_all2)
    button_3_2.pack()

    frame_4=tk.Frame(window)
    frame_4.place(x=0, y=0, width=400, height=600)
    for i in range(len(c_sta)):
        globals()['s_CheckVar{}'.format(i)] = tk.IntVar()
        globals()['s{}'.format(i)] = tk.Checkbutton(frame_4, text="{}".format(c_sta[i]),
                                                    variable=eval('s_CheckVar{}'.format(i)))
        globals()['s{}'.format(i)].pack()
    button_4_1=tk.Button(frame_4,text='확인',command=move_toFrame5)
    button_4_1.pack()
    button_4_2=tk.Button(frame_4,text='모두 선택',command=check_all3)
    button_4_2.pack()

    frame_5=tk.Frame(window)
    frame_5.place(x=0, y=0, width=400, height=600)
    for i in range(len(c_y)):
        globals()['y_CheckVar{}'.format(i)] = tk.IntVar()
        globals()['y{}'.format(i)] = tk.Checkbutton(frame_5, text="{}".format(c_y[i]),
                                                    variable=eval('y_CheckVar{}'.format(i)))
        globals()['y{}'.format(i)].pack()
    button_5_1=tk.Button(frame_5,text='확인',command=move_toFrame6)
    button_5_1.pack()
    button_5_2=tk.Button(frame_5,text='모두 선택',command=check_all4)
    button_5_2.pack()

    frame_1=tk.Frame(window)
    frame_1.place(x=0,y=0, width=400, height=600)
    for i in range(len(city_n)):
        globals()['CheckVar{}'.format(i)] = tk.IntVar()
        globals()['c{}'.format(i)] = tk.Checkbutton(frame_1, text="{}".format(city_n[i]),
                                                    variable=eval('CheckVar{}'.format(i)))
        globals()['c{}'.format(i)].pack()
    button_1=tk.Button(frame_1,text='확인',command=move_toFrame2)
    button_1.pack()
    button_2=tk.Button(frame_1,text='모두 선택',command=check_all)
    button_2.pack()

    window.mainloop()
