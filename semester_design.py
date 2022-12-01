
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


def tkinter_matplolib():
    # the figure that will contain the plot
    fig = Figure(figsize=(5, 5), dpi=100)

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


class sem_analyze():
    def __init__(self):
        self.attendence = 0  # 출석율
        self.asm_rate = 0  # 과제 제출율
        self.quiz_rate = 0  # 퀴즈 제출율
        self.grade = 0  # 총 학점
        self.lecatt = 0  # 수강 갯수
        self.asm_quiz_grade = 0  # 퀴즈 과제에 따른 점수
        self.mjr_lecture = 0  # 전공 갯수
        self.asmnum = 0  # 과제 갯수
        self.quiznum = 0  # 퀴즈 갯수

    def mjr_lec_score(self):
        score = 0
        if self.mjr_lecture >= 6:
            score = 100
        elif self.mjr_lecture >= 5:
            score = 80
        elif self.mjr_lecture >= 4:
            score = 70
        elif self.mjr_lecture >= 3:
            score = 60
        return score

    def asm_quiz_score(self):
        score = 0
        if (self.asmnum+self.quiznum) >= 10:
            score = 5
        elif (self.asmnum+self.quiznum) < 10 or (self.asmnum+self.quiznum) >= 5:
            score = 3
        elif (self.asmnum+self.quiznum) < 5 or (self.asmnum+self.quiznum) >= 3:
            score = 1
        else:
            score = 0
        return score

    def willpower(self):  # 의지력
        return (self.attendence+self.asm_rate +
        self.quiz_rate)/100

    def intellect(self):  # 지능
        return (self.grade)/(self.lecatt*5)
    # (총 학점 ) / (수강 갯수 * 4.5)
    # 생존력

    def viabiltiy(self):
        score = self.asm_quiz_score(self)
        return score / (self.lecatt * 5)
    # (총 과제, 퀴즈에 따른 점수) / (수강 과목 갯수 * 5)

    # 근면성
    def dilligence(self):
        score = self.mjr_lec_score(self)
        return score / 100

    # ( 전공갯수에 따른 점수 ) / 100

    # 가성비

    def cost_benefit(self):
        return self.intellect(self)/self.willpower(self)
    # (지능 /의지력)


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
a = fig.add_subplot()
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

canvas.get_tk_widget().place(x= 200, y=500)

tkinter.mainloop()



 #그래프 보이게 하기
# data = [6, 5, 4, 6, 2]
# reg_pentagon_graph(10, data)
# plt.show()




# 가로가 깨지는 모습??

# semester는 년도와 학기 
# message = tkinter.Message(window,text=inpsemester,width =400, relief="flat")

# #ID는 학번
# Id=tkinter.Message(window,text=inpId,width =400, relief="flat")

# # Name 은 이름
# Name = tkinter.Message(window,text= inpName,width = 400, relief="flat")



# message.pack()

# text = tkinter.Text(window)

# text.insert(tkinter.CURRENT,inpsemester)
# text.insert("current","\t\t\t")
# text.insert("current",inpId)
# text.insert("current","\t")
# text.insert("current",inpName)


# text.pack()


# plot_button = Button(master = window, 
#                      command = plt,
#                      height = 2, 
#                      width = 10,
#                      text = "Plot")


# plot_button.pack()
