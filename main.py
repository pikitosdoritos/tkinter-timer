import tkinter
from tkinter import messagebox

seconds = 9

window = tkinter.Tk()

window.title("Timer")
window.geometry("400x400+2800+300")

label = tkinter.Label(window, text=str(seconds))
label.pack(pady=10)

def countdown():
    global seconds
    
    if seconds < 0:
        return
    
    window.after(1000, countdown)
    label.config(text=str(seconds))

    seconds -= 1

countdown()

window.mainloop()