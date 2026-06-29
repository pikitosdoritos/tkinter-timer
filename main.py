import tkinter
from tkinter import messagebox
import time

timer = 9

window = tkinter.Tk()

window.title("Timer")
window.geometry("400x400+2800+300")

label = tkinter.Label(window, text=str(timer))
label.pack(pady=10)

window.after(1000, lambda: label.config(text="8"))

window.mainloop()