from cProfile import label
from tkinter import *
import tkinter
from tokenize import Name
from turtle import color
from unittest import result
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)


plt.rc('font', family='NanumGothic')


def reg_pentagon_list(inp):
        # Max_pos = max(inp)
        # Max_pos_x = []
        # Max_pos_y = []
        result_x = []
        result_y = []  
        for i in range(5):
            theta = (2*np.pi / 5) * (i+1) - (3*np.pi/10)
            result_x.append(inp[i]*np.cos(theta))
            result_y.append(inp[i]*np.sin(theta))
            # Max_pos_x.append(Max_pos*np.cos(theta))
            # Max_pos_y.append(Max_pos*np.sin(theta))
        theta = (2*np.pi / 5) * (0+1) - (3*np.pi/10)
        result_x.append(inp[0]*np.cos(theta))
        result_y.append(inp[0]*np.sin(theta))
        return result_x, result_y


def reg_pentagon_graph(inp1, inp2):
        max_list = np.zeros(5)+inp1
        max_x, max_y = reg_pentagon_list(max_list)
        x, y = reg_pentagon_list(inp2)
        fig, ax = plt.subplots()
        fig.set_size_inches(10, 10)
        ax.axis('off')
         # 바깥족 그래프
        plt.plot(max_x, max_y, 'r')

        # 안쪽 그래프
        plt.plot(x, y, 'r')

        # 색채우기
        plt.fill_between(x, y, 0, facecolor="red", alpha=0.2)

        # 점수 쓰기
        score_list = np.array(inp2)+1
        score_x, score_y = reg_pentagon_list(score_list)
        # 글자 쓰기
        text = ['의지력', '지능', '생존력', '근면성', '가성비']
        text_x, text_y = reg_pentagon_list(max_list+1)
        for i in range(5):
        # 점수
            plt.text(score_x[i], score_y[i], inp2[i], fontsize=18)
        # 점선
            plt.plot([0, max_x[i]], [0, max_y[i]],
                     linestyle='--', color='gray')
        # 글자
            plt.text(text_x[i], text_y[i], text[i], fontsize=15)

window = Tk()
# window.configure(bg="green") # 배경색 설정
window.title("semester")
window.geometry("1000x1000")
window.resizable(False, False)
# window.option_add("*Font","맑은고딕 20")

# 함수 받아서 넣기
willpower_rate = 6  # 의지력 점수
intellect_rate = 5   # 지능 점수
viabiltiy_rate = 4    # 생존력 점수
dilligence_rate = 6    # 근면성 점수
cost_benefit_rate = 2  # 가성비 점수

# 크롤링해서 받아서 저장한 정보를 넣기
inpsemester = "2021학년도 1학기"
inpId = "2021203043"
inpName = "김동현"

fig = Figure(figsize=(150,250),dpi =100)
a = fig.add_subplot(2,2,1)
a.axis('off')

data = [willpower_rate, intellect_rate, viabiltiy_rate, 
        dilligence_rate, cost_benefit_rate]
result_x = []
result_y = []
for i in range(5):
            theta = (2*np.pi / 5) * (i+1) - (3*np.pi/10)
            result_x.append(data[i]*np.cos(theta))
            result_y.append(data[i]*np.sin(theta))
            # Max_pos_x.append(Max_pos*np.cos(theta))
            # Max_pos_y.append(Max_pos*np.sin(theta))
theta = (2*np.pi / 5) * (0+1) - (3*np.pi/10)
result_x.append(data[0]*np.cos(theta))
result_y.append(data[0]*np.sin(theta))

max_list = np.zeros(5)+10
max_x, max_y = reg_pentagon_list(max_list)
x, y = result_x,result_y 

         # 바깥족 그래프
a.plot(max_x, max_y, 'r')

        # 안쪽 그래프
a.plot(x, y, 'r')

        # 색채우기
a.fill_between(x, y, 0, facecolor="red", alpha=0.2)

        # 점수 쓰기
score_list = np.array(data)+1
score_x, score_y = reg_pentagon_list(score_list)
        # 글자 쓰기
text = ['의지력', '지능', '생존력', '근면성', '가성비']
text_x, text_y = reg_pentagon_list(max_list+1)
for i in range(5):
    # 점수
    a.text(score_x[i], score_y[i], data[i], fontsize=18)
    # 점선
    a.plot([0, max_x[i]], [0, max_y[i]],
                     linestyle='--', color='gray')
    # 글자
    a.text(text_x[i], text_y[i], text[i], fontsize=15)

# wcanvas = Canvas(window, width= 100, height= 500)
# wcanvas.pack()

canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
canvas.draw()
# canvas.get_tk_widget().pack()
canvas.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=True)


# a = fig.add_subplot(111)
# data = [6, 5, 4, 6, 2]

# a.reg_pentagon_graph(10,data)

# canvas = FigureCanvasTkAgg(fig, master=window)
# canvas.draw()



tkinter.Label(text=inpsemester,width=10,font="맑은고딕 25",padx=100).place(x=100,y=0)
tkinter.Label(text=inpId,font="맑은고딕 25",width=10).place(x=600,y=0)
tkinter.Label(text=inpName,font="맑은고딕 25",width=10).place(x=800,y=0)

tkinter.Label(text="의지력",font="맑은고딕 20",width=10).place(x=700,y=200)
tkinter.Label(text=willpower_rate,font="맑은고딕 20",width=10).place(x=800,y=250)

# tkinter.Label(text="의지력 \n" ,textvariable = willpower_rate,width=10).place(x=700,y=200)

tkinter.Label(text="지능",font="맑은고딕 20",width=10).place(x=700,y=300)
tkinter.Label(text=intellect_rate,font="맑은고딕 20",width=10).place(x=800,y=350)

tkinter.Label(text="생존력",font="맑은고딕 20",width=10).place(x=700,y=400)
tkinter.Label(text=viabiltiy_rate,font="맑은고딕 20",width=10).place(x=800,y=450)

tkinter.Label(text="근면성",font="맑은고딕 20",width=10).place(x=700,y=500)
tkinter.Label(text=dilligence_rate,font="맑은고딕 20",width=10).place(x=800,y=550)

tkinter.Label(text="가성비",font="맑은고딕 20",width=10).place(x=700,y=600)
tkinter.Label(text=cost_benefit_rate,font="맑은고딕 20",width=10).place(x=800,y=650)



tkinter.mainloop()
