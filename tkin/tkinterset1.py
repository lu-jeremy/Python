import tkinter
from tkinter import messagebox

def print_text():
    text1 = e1.get()
    text2 = e2.get()
    tkinter.messagebox.showinfo('First name',text1+' '+text2)
    
def clear():
    e1.delete(0,tkinter.END)
    e2.delete(0,tkinter.END)
    
root = tkinter.Tk()

f = tkinter.Label(root, text = 'First name')
e1 = tkinter.Entry(root)

l = tkinter.Label(root, text = 'Last name')
e2 = tkinter.Entry(root)

email = tkinter.Label(root, text = 'Email')
e3 = tkinter.Entry(root)
phone = tkinter.Label(root, text = 'Phone #')
e4 = tkinter.Entry(root)

p = tkinter.Button(root, text = 'Print', command = print_text)
c = tkinter.Button(root, text = 'Clear', command = clear)
q = tkinter.Button(root, text = 'Quit', command = exit)


f.grid(row = 0, column = 0)
e1.grid(row = 0, column = 1)

l.grid(row = 1, column = 0)
e2.grid(row = 1,column = 1)

email.grid(row = 2, column = 0)
e3.grid(row = 2, column  = 1)

phone.grid(row = 3, column = 0)
e4.grid(row = 3, column = 1)

p.grid(row = 4, column = 0)
c.grid(row = 4, column = 1)
q.grid(row = 4,column = 2)

root.title('My first App')

root.mainloop()


