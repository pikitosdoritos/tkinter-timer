import tkinter
from tkinter import messagebox

seconds = 9

def countdown():
    global seconds
    
    if seconds < 0:
        return
    
    window.after(1000, countdown)
    label.config(text=str(seconds))

    seconds -= 1

window = tkinter.Tk()

window.title("Timer")
window.geometry("400x400+2800+300")

label = tkinter.Label(window)
label.pack(pady=10)

input_field = tkinter.Entry(window, width=50)
input_field.pack(pady=30)

button = tkinter.Button(window, text="Start", command=countdown)
button.pack(pady=100)

window.mainloop()