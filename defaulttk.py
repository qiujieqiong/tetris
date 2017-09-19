#/usr/bin/env python3
#-*- coding=utf-8 -*-
from tkinter import *
from time import sleep
import threading

root = Tk()                     # 创建窗口对象的背景色
root.title("fang kuai")
bsize=15

class Config:
    x=6
    @staticmethod
    def reset():
        Config.x=6


def right(event):
    if Config.x < 10:
        Config.x=Config.x+1

def left(event):
    if Config.x>1:
        Config.x=Config.x-1

root.bind("<Left>",left)
root.bind("<Right>",right)
#root.bind("<Up>",left)
#root.bind("<Down>",right)

a=[ [0 for y in range(12) ] for x in range(20) ]

def clear(yy):
    m =[ cm for cm in a[yy][1:11] if cm ==0 ]
    if m==[]:
        #清除效果
        for emm in range(3):
            for cm in a[yy][1:11]:
                cm["bg"]="green"
                cm["fg"]= "green"
            sleep(0.15)
            for cm in a[yy][1:11]:
                cm["bg"]="red"
                cm["fg"]= "red"
            sleep(0.15)
        #清除方块
        for cm in a[yy][1:11]:
            cm.destroy()
        for x in range(yy,0,-1):
            a[x]=a[x-1]
            for ei in range(12):
                if a[x][ei] != 0:
                    a[x][ei].grid(row=x,column=ei)
        a[0]=[0 for y in range(12)]

def mm():
    xia = Button(master=root, bitmap="gray50", height=bsize, width=bsize, bg="red", fg="red",bd=0)
    Config.reset()
    for y in range(1,19):
        xia.grid(row=y, column=Config.x)
        sleep(0.1)
        if a[y+1][Config.x] !=0 or y==18:#判断下面有没方块,有就停
            a[y][Config.x]=xia#记录当前位置已有方块
            clear(y)
            break

    mm()
t = threading.Thread(target=mm)
t.setDaemon(True)
t.start()

#边框
for x in range(12):
    b = Button(master=root, bitmap="gray50", height=bsize, width=bsize,bd=0)
    b.grid(row=0, column=x)
    b = Button(master=root, bitmap="gray50", height=bsize, width=bsize,bd=0)
    b.grid(row=19, column=x)
for x in range(20):
    b = Button(master=root, bitmap="gray50", height=bsize, width=bsize,bd=0)
    b.grid(row=x, column=0)
    b = Button(master=root, bitmap="gray50", height=bsize, width=bsize,bd=0)
    b.grid(row=x, column=11)


root.mainloop()