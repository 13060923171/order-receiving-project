from tkinter import *
import tkinter as tk
from tkinter.tix import Tk, Control, ComboBox  #升级的组合控件包
from tkinter.messagebox import showinfo, showwarning, showerror #各种类型的提示框
from tkinter import ttk
from tkinter import filedialog
import cv2
import main02
import time
import datetime
import eventlet
from PIL import Image, ImageTk
class CanvasDemo:
    def __init__(self):
        # 创建windows窗口对象,初始化TK
        # colors = '''#FFB6C1'''
        # window = Toplevel()
        window = tk.Tk()

        # i=0
        # colcut = 5
        ##设置窗口透明度从0-1，1是不透明，0是全透明
        window.wm_attributes("-alpha", 1)

        #设置窗口标题
        window.title("人脸衰老")
        window.config(bg = '#2B2B2B')  ##2B2B2B/#1b1c26
        #设置窗口图标
        # window.iconbitmap(r'G:\qita\sky.ico')
        # window.iconphoto(False, tk.PhotoImage(file=r'G:\qita\qianyi.png'))
        # 设置窗口大小
        window.geometry("600x800")
        # window.geometry()
        # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
        window.resizable(width=False, height=False)
        #window.resizable(1,1)
        window.resizable()
        #通过配置TNotebook样式的tabposition选项来更改选项卡的位置
        start = time.clock()

        # def func(a, b):
        #     while True:
        #         end = time.clock()
        #     if int(end - start) == 10:
        #         print('Warning: Timeout!!' * 5)
        #         return break
        # a = a + b
        #
        # print(a)
        # func(1, 2)



        def resize(w, h, w_box, h_box, image):
            '''
            resize a pil_image object so it will fit into
            a box of size w_box times h_box, but retain aspect ratio
            对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例
            '''
            f1 = 1.0 * w_box / w  # 1.0 forces float division in Python2
            f2 = 1.0 * h_box / h
            factor = min([f1, f2])
            # print(f1, f2, factor) # test
            # use best down-sizing filter
            width = int(w * factor)
            height = int(h * factor)
            return image.resize((width, height), Image.ANTIALIAS)




        global img_counter
        def camera():
            window.destroy()
            main02.CanvasDemo2().showCanvasDemo2()
        # 期望图像显示的大小
        w_box = 1080
        h_box = 1920

        image = Image.open("1.jpg")

        # 获取图像的原始大小
        # w, h = image.size

        # 缩放图像让它保持比例，同时限制在一个矩形框范围内
        # image_resized = resize(w, h, w_box, h_box, image)

        im = ImageTk.PhotoImage(image)

        # file = PhotoImage("zhu01.jpg")
        backlabel = Label(window, image=im,width=w_box, height=h_box)
        backlabel.pack(fill="both",expand='Yes')
        # backlabel.place(x=0, y=0, relwidth=1, relheight=1)
        # b1 = Button(window, text="开始体验", bg="Tomato", bd=12, command=camera)
        b1 = Button(window, text="开始体验", bg="Tomato",  command=camera)
        # b1.grid()
        b1.place(x=190,y=490)

        b2 = Button(window, text="开始体验", fg="#2b2b2b",bg="Tomato", command=camera)
        # b1.grid()
        b2.place(x=360, y=490)
########################显示器##################################
        #获取屏幕宽和高
        screenwidth1 = window.winfo_screenwidth()  # 获取屏幕宽度（单位：像素）
        screenheight1 = window.winfo_screenheight()  # 获取屏幕高度（单位：像素）
        #获取窗口宽和高
        window_width = window.winfo_width()  # 获取窗口宽度（单位：像素）
        window_height = window.winfo_height()  # 获取窗口高度（单位：像素）
        #窗口刷新
        window.update()
        print("屏幕分辨率：",screenwidth1,screenheight1)
        print(datetime.datetime.now())
        window.mainloop()
        eventlet.monkey_patch()  # 必须加这条代码
        with eventlet.Timeout(200000, False):
            time.sleep(40000)
            window.destroyWindow()
            print('没有跳过这条输出')
        start = time.clock()
        end = time.clock()
        t = end - start
        print("Runtime is ：", t)

if __name__=='__main__':

    CanvasDemo()