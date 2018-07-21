import tkinter

root = tkinter.Tk()

root.title('4')
choice = tkinter.StringVar(root)
choice.set('Choices')
drop_down = tkinter.OptionMenu(root,choice,'Meters To Inches','Inches To Meters')
drop_down.grid(row = 3, column = 0)
def thing():
    print(choice.get())
    if choice.get() == 'Meters To Inches':
        m_i()
    if choice.get() == 'Inches To Meters':
        i_m()
def m_i():
    get1 = int(m_e.get())
    i = (get1)*39
    i_e.insert(0,i)
def clear():
    i_e.delete(0,tkinter.END)
    m_e.delete(0,tkinter.END)
def i_m():
    get2 = int(i_e.get())
    m = (get2)/39
    m_e.insert(0,m)
meters = tkinter.Label(root, text =  'Meters')
m_e = tkinter.Entry(root)

inches = tkinter.Label(root, text = 'Inches')
i_e = tkinter.Entry(root)

convert = tkinter.Button(root, text = 'Convert!',command = thing)
clear = tkinter.Button(root, text= 'Clear entry',command = clear)

meters.grid(row = 0, column = 0)
m_e.grid(row = 0, column = 1)
inches.grid(row = 1, column = 0)
i_e.grid(row = 1, column = 1)
         
convert.grid(row = 2, column = 0)
clear.grid(row = 2, column = 1)

root.mainloop()
