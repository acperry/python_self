from tkinter import *

def processOK():
    print("ok button is clicked")

def processCancel():
    print("cancel button is clicked")

window = Tk()

btOK = Button(window, text = 'ok', fg= 'red', command= processOK)

btCancel = Button(window, text = 'Cancel', fg= 'yellow', command= processCancel)

btOK.pack()
btCancel.pack()

window.mainloop()