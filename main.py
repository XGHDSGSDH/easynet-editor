from tkinter import *
import random
from editor import editor
from layer import layer
from tensor import tensor

window=Tk()
window.title("Easynet")
window.state("zoomed")
window.resizable(width=False, height=False)
#print(window.winfo_x(),window.winfo_width(),window.winfo_y(),window.winfo_height())
window.update()
new_editor=editor(window.winfo_x()+window.winfo_width()/2,window.winfo_y()+window.winfo_height()/2, window)
window.mainloop()