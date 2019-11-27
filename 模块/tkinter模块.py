# coding= utf-8
from tkinter import Tk, Label
from tkinter import Button, Entry,Text
import tkinter
# 创建主窗口
win = Tk()
# 标题
win.title("my window")

# 设置窗口大小和位置(x,y的位置坐标)
win.geometry("500x500+100+100")
#进入消息循环
# Label组件，可以显示文本和位圈
#anchor 位置：N NE E SE S SW WN W CETER
# label =Label(win, text="tonyis good man ", bg="blue", font=("Arial", 15))
#wraplength指定text 文件多少宽度后换行
# justify 多行文本对齐方式
# l =Label(win, text='你好！this is Tkinter', bg='green', font=('Arial', 12),
#          anchor=tkinter.NE, width=30, height=2,wraplength =100,justify = "right")
# #显示控件
# l.pack()
# height 控制显示行数
t = tkinter.Text(win, width=4,height=1)
# t.pack()
t.pack(side=tkinter.LEFT, fill=tkinter.Y) #滚动条写法
info = """
酒店列表说明：
用户扫描酒店小程序，并且在手机号授权后，显示该手机号下面所有酒店。
"""
t.insert(tkinter.INSERT, info)
# 输入控件 类似输入框 entry
#textvariable 绑定文本变量，在代码的其他位置通过变量获取或设置该控件的内容
info = tkinter.Variable()
entry = Entry(win, textvariable=info)
entrypasswd = Entry(win,show="*")
entry.pack()
entrypasswd.pack()

def func1():
    print("entry 内容%s" %(info.get()) )
    info.set("good")  # 绑定赋值
# 按钮控件 button
button = Button(win, text="按钮1", width=10, height=10, command=func1, bg= "red")
button.pack()
#程序运行起来
win.mainloop()
