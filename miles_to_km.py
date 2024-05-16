from tkinter import *

window = Tk()
window.minsize(height=150,width=250)
window.config(padx=20,pady=20)
window.title("Mile to Km converter")

entry = Entry(width=10)
entry.insert(END,string='0')
entry.grid(column=1,row=0)

l1 = Label(text='Miles')
l1.grid(column=2,row=0)

l2 = Label(text='is equal to')
l2.grid(column=0,row=1)

l3 = Label(text='0')
l3.grid(column=1,row=1)

l4 = Label(text='Km')
l4.grid(column=2,row=1)

def b1_click():
    x = entry.get()
    x = float(x)
    x = x * 1.60934
    l3.config(text=x)

b1 = Button(text='Calculate',command=b1_click)
b1.grid(column=1,row=2)

window.mainloop()
