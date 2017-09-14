#/usr/bin/env python3
#-*- coding=utf-8 -*-

from  tkinter import  *
import threading
from time import sleep

root = Tk()                     # 创建窗口对象的背景色
root.title("fang kuai")
bsize=15

def mm():
    xia = Button(master=root, bitmap="gray25", height=bsize, width=bsize, bg="red", fg="red",bd=0)

    for x in range(1,19):
        xia.grid(row=x, column=6)
        sleep(0.3)

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