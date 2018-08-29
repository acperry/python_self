from tkinter import *

window = Tk()
label = Label(window, text='welcome to python GUI')
button = Button(window, text = 'Click Me')
label.pack()
button.pack()

window.mainloop()