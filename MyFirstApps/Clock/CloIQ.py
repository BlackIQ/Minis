from tkinter import *
from time import *

win = Tk()
win.title("CloIQ")
win.resizable(0, 0)

time1 = ''
clock = Label(win, font = ('Tahoma', 50), fg = "#008B8B", bg = "white")
clock.pack(fill = BOTH, expand = 1)


def tick():
    time1 = gmtime()
    time2 = strftime("%H:%M:%S", time1)

    clock.config(text = time2)
        
    clock.after(200, tick)
        
tick()
win.mainloop()
