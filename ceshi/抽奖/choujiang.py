import time
import random
from multiprocessing import Process
import tkinter as tk
import threading

top = tk.Tk()
top.geometry('600x400')
top.title('抽奖器')

li = ['Jhon', 'Alex', 'xiaoma', 'Kingkong', 'Boby']
b_state = 1


def func1():
    while b_state == 1:
        for i in li:
            label = tk.Label(top, text=i)
            label.pack()

top.mainloop()

t1 = Process(target=func1, args=())
t1.start()
t1.join()

