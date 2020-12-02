from tkinter import *
import tkinter as tk
from tkinter.tix import Tk, Control, ComboBox  #升级的组合控件包
from tkinter.messagebox import showinfo, showwarning, showerror #各种类型的提示框
from tkinter import ttk
from tkinter import filedialog
import cv2
import threading
from PIL import Image, ImageTk

class CanvasDemo2:
    def __init__(self):
        self.camera = None  # 摄像头
        self.root = Tk()
        self.root.title('人脸衰老')
        self.root.geometry('%dx%d' % (800, 600))
        self.createFirstPage()
        mainloop()

    def createFirstPage(self):
        self.page1 = Frame(self.root)
        self.page1.pack()
        self.button12 = Button(self.page1, width=18, height=2, text="录入新的人脸", bg='green', font=("宋", 12),
                               relief='raise', command=self.createSecondPage)
        self.button12.pack(side=LEFT, padx=25, pady=10)
    def createSecondPage(self):
        image = Image.open(r'3.jpg')
        background_image = ImageTk.PhotoImage(image)
        w = background_image.width()
        h = background_image.height()
        self.root.geometry('%dx%d+0+0' % (w, h))
        background_label = Label(self.root, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.camera = cv2.VideoCapture(0)
        self.page2 = Frame(self.root)
        self.page2.pack()
        self.data2 = Label(self.page2,width=410, height=490)
        self.data2.pack(side=RIGHT,padx=0, pady=0,expand=YES,fill='y')
        txt = tk.StringVar()
        text5 = tk.Entry(self.root, textvariable=txt, font='Helvetica 12 bold', bg='white', width=20).place(x=250, y=695)
        txt.set('30岁的你')
        # backlabel.place(x=0, y=0, relwidth=1, relheight=1)
        b1 = Button(self.root, text="返回", width=5, height=1, bg="blue", fg="white", command=self.backFirst)
        # b1.grid()
        b1.place(x=110, y=740)
        self.video_loop(self.data2)
        mainloop()

    def video_loop(self, panela):

        success, img = self.camera.read()  # 从摄像头读取照片
        if success:
            cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)  # 转换颜色从BGR到RGBA
            current_image = Image.fromarray(cv2image)  # 将图像转换成Image对象
            imgtk = ImageTk.PhotoImage(image=current_image)
            panela.imgtk = imgtk
            panela.config(image=imgtk)
            self.root.after(1, lambda: self.video_loop(panela))

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
    CanvasDemo2()