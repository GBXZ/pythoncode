import time
import random
from multiprocessing import Process
import tkinter as tk
import threading

a_list = []
b_state = 1
a = 0


def b_input(li):
    while b_state == 1:
        for i in li:
            print(i)
            time.sleep(0.1)


def main(*args):
    top = tk.Tk()
    top.geometry('600x400')

    def func():
        global b_state
        b_state = 0
        label = tk.Label(top, text=random.choice(args))
        label.pack()
    button = tk.Button(top, text='暂停', command=func)
    button.pack()
    top.mainloop()


if __name__ == '__main__':
    l1 = ['Jhon', 'Alex', 'xiaoma', 'Kingkong', 'Boby']
    P1 = threading.Thread(target=main, args=(l1))
    P2 = threading.Thread(target=b_input, args=(['Jhon', 'Alex', 'xiaoma', 'Kingkong', 'Boby'], ))
    P1.start()
    P2.start()
    P2.join()
    P1.join()

