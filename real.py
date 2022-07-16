import tkinter as tk 
window = tk.Tk()
window.title('tk')
subtotal = 20.04
price = 0
tax = 4.45
total = 38.87


btn1 = tk.Button(window, text='Add product',command=lambda:subtotal+1)
btn2 = tk.Button(window, text='Check Out')
tk.Label(window, text="Joe's Sporting Goods ",
         justify='center', font='bold').grid(row=0, column=0)

tk.Label(window, text= "Cost:  ",fg="purple").grid(row=1,column=0)
tk.Entry(window, text=price).grid(row=1, column=1)
btn1.grid(row=3, column=0)
btn2.grid(row=3,column=1)


tk.Label(window, text="Subtotal:  ").grid(row=2, column=0)
tk.Label(window, text=subtotal).grid(row=2, column=1)

tk.Label(window, text="Tax:  ").grid(row=4, column=0)
tk.Label(window, text=tax).grid(row=4, column=1)

tk.Label(window, text="Tax:  ").grid(row=5, column=0)
tk.Label(window, text=total).grid(row=5, column=1)
window.mainloop()