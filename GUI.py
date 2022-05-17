from tkinter import *
from tkinter import messagebox


root = Tk()
btn01 =Button(root)
root.title("商品信息管理系统")
root.geometry("500x400+100+200") #宽度 500，高度 400；距 屏幕左边 100，距屏幕上边 200
btn01['text'] = "点击进入商品信息管理系统"
btn01.pack()# 布局管理器

def fun(e):#e就是事件对象
     messagebox.showinfo("Message","系统功能待开发")# Message是标题

btn01.bind("<Button-1>",fun)# 进行事件的绑定
root.mainloop() # 调用组件的mainloop方法，进入事件循环
