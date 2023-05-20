import sys
from tkinter import *
from binlogUtil import command_line_args

win = Tk()
input_box = Entry(win, width=60)
# 显示按钮
input_box.pack()


def on_button_click(name):
    print(f"{name} clicked!", input_box.get())


but = Button(win, text="确认", command=lambda: on_button_click("Button 1"))
but.pack()

win.geometry("300x200")
win.mainloop()


if __name__ == '__main__':
    print(sys.argv[1:])
    args = command_line_args(sys.argv[1:])
