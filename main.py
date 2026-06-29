import tkinter
from tkinter import messagebox

seconds = 9

def countdown():
    global seconds
    
    if seconds < 0:
        input_field.pack(pady=10)
        button.pack(pady=10)
        return
    
    window.after(1000, countdown)
    label.config(text=str(seconds))

    seconds -= 1

def start():
    global seconds
    
    seconds = int(input_field.get())

    input_field.pack_forget()
    button.pack_forget()

    countdown()

window = tkinter.Tk()

window.title("Timer")
window.geometry("400x400+2800+300")

label = tkinter.Label(window)
label.pack(pady=10)

input_field = tkinter.Entry(window, width=50)
input_field.pack(pady=10)

button = tkinter.Button(window, text="Start", command=start)
button.pack(pady=10)

window.mainloop()