from tkinter import *
import cv2
import os
from PIL import Image, ImageTk
from tkinter import ttk
# from multiprocessing import Process
# import facial_recognition
# import database

class APP:
    def __init__(self):
        self.camera = None   # 摄像头
        self.root = Tk()
        self.root.title('FACE')
        self.root.geometry('%dx%d' % (800, 600))
        self.createFirstPage()
        mainloop()

    def createFirstPage(self):
        self.page1 = Frame(self.root)
        self.page1.pack()
        Label(self.page1, text='欢迎使用人脸识别系统', font=('粗体', 20)).pack()
        image = Image.open("face.png") #随便使用一张图片 不要太大
        photo = ImageTk.PhotoImage(image = image)
        self.data1 = Label(self.page1,  width=780,image = photo)
        self.data1.image = photo
        self.data1.pack(padx=5, pady=5)

        self.button11 = Button(self.page1, width=18, height=2, text="签到打卡", bg='red', font=("宋", 12),
                               relief='raise',command = self.createSecondPage)
        self.button11.pack(side=LEFT, padx=25, pady = 10)
        self.button12 = Button(self.page1, width=18, height=2, text="录入新的人脸", bg='green', font=("宋", 12),
                               relief='raise', command = self.createSecondPage)
        self.button12.pack(side=LEFT, padx=25, pady = 10)
        self.button13 = Button(self.page1, width=18, height=2, text="查询签到信息", bg='white', font=("宋", 12), relief='raise',
                               command = self.checkDataView)
        self.button13.pack(side=LEFT, padx=25, pady = 10)
        self.button14 = Button(self.page1, width=18, height=2, text="退出系统", bg='gray', font=("宋", 12),
                               relief='raise',command = self.quitMain)
        self.button14.pack(side=LEFT, padx=25, pady = 10)

    def createSecondPage(self):
        self.camera = cv2.VideoCapture(0)
        self.page1.pack_forget()
        self.page2 = Frame(self.root)
        self.page2.pack()
        Label(self.page2, text='欢迎使用人脸识别系统', font=('粗体', 20)).pack()
        self.data2 = Label(self.page2)
        self.data2.pack(padx=5, pady=5)

        self.button21 = Button(self.page2, width=18, height=2, text="返回", bg='gray', font=("宋", 12),
                               relief='raise',command = self.backFirst)
        self.button21.pack(padx=25,pady = 10)
        self.video_loop(self.data2)

    def video_loop(self, panela):

        success, img = self.camera.read()  # 从摄像头读取照片
        if success:
            cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)  # 转换颜色从BGR到RGBA
            current_image = Image.fromarray(cv2image)  # 将图像转换成Image对象
            imgtk = ImageTk.PhotoImage(image=current_image)
            panela.imgtk = imgtk
            panela.config(image=imgtk)
            self.root.after(1, lambda: self.video_loop(panela))

    #  签到信息展示
    # noinspection PyAttributeOutsideInit
    def checkDataView(self):
        self.page3 = Frame(self.root)
        self.page1.pack_forget()
        self.root.geometry('700x360')
        Label(self.page3, text='今日签到信息', bg='white', fg='red', font=('宋体', 25)).pack(side=TOP, fill='x')
        self.checkDate = ttk.Treeview(self.page3, show='headings', column=('sid', 'name', 'check_time' ))

        self.checkDate.column('sid', width=100, anchor="center")
        self.checkDate.column('name', width=200, anchor="center")
        self.checkDate.column('check_time', width=300, anchor="center")


        self.checkDate.heading('sid', text='签到序号')
        self.checkDate.heading('name', text='名字')
        self.checkDate.heading('check_time', text='签到时间')



        self.checkDate.pack(expand = 1, fill = BOTH)
        Button(self.page3, width=20, height=2, text="返回", bg='gray', font=("宋", 12),
               relief='raise',command =self.backMain).pack(padx = 20, pady = 20)
        self.page3.pack()



    def backFirst(self):
        self.page2.pack_forget()
        self.page1.pack()
        # 释放摄像头资源
        self.camera.release()
        cv2.destroyAllWindows()

    def backMain(self):
        self.root.geometry('900x600')
        self.page3.pack_forget()
        self.page1.pack()

    def quitMain(self):
        sys.exit(0)


if __name__ == '__main__':

    demo = APP()