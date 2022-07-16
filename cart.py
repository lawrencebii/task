import tkinter as tk

window = tk.Tk()
window.title('Carting')

top_frame = tk.Frame(window).pack()
bottom_frame = tk.Frame(window).pack(side='bottom')
btn1 = tk.Button(top_frame, text='Button1', fg='red').pack()
btn2 = tk.Button(top_frame, text='Button2', fg='green').pack()
btn3 = tk.Button(bottom_frame, text='Button3', fg='purple').pack()
btn4 = tk.Button(bottom_frame, text='Button4', fg='orange').pack()

window.mainloop()
