import tkinter
import time

root = tkinter.Tk()


root.title('6')

#eval(), bitbucket
#columnspan
#write it as class

#display = tkinter.Entry(root)
#display1 = tkinter.Entry(root)
result = tkinter.Entry(root,justify = tkinter.RIGHT,bg = "orange",font = 'Garamond 22 bold',width = 50)
def common(n):
    result.insert(tkinter.END,n)
def equal():
    if result.get()!='':
        get1 = result.get()
        r_ev = eval(get1)
        result.delete(0,tkinter.END)
        result.insert(tkinter.END,r_ev)
def clearing():
    result.delete(0,tkinter.END)
addition = tkinter.Button(root, text = '+',command = lambda:common('+'))
subtraction = tkinter.Button(root, text = '-',command = lambda:common('-'))
multiplication = tkinter.Button(root, text = 'x',command = lambda:common('*'))
division = tkinter.Button(root, text = '/',command = lambda:common('/'))
power = tkinter.Button(root, text = '^',command = lambda:common('**'))

one = tkinter.Button(root, text = '1',command = lambda:common(1))
two = tkinter.Button(root, text = '2',command = lambda:common(2))
three = tkinter.Button(root, text = '3',command = lambda:common(3))
four = tkinter.Button(root, text = '4',command = lambda:common(4))
five = tkinter.Button(root, text = '5',command = lambda:common(5))
six = tkinter.Button(root, text = '6',command = lambda:common(6))
seven = tkinter.Button(root, text = '7',command = lambda:common(7))
eight = tkinter.Button(root, text = '8',command = lambda:common(8))
nine = tkinter.Button(root, text = '9',command = lambda:common(9))

equals = tkinter.Button(root, text = '=', command = equal)
clear = tkinter.Button(root, text = 'Clear', width = 10,command = clearing)

#display1.grid(row = 0, column = 1)
#display.grid(row = 0, column = 0)
result.grid(row = 0, column = 0, columnspan = 10)

equals.grid(row = 1, column = 0,rowspan =2, sticky = 'NSEW')
addition.grid(row = 1, column = 1)
subtraction.grid(row =1, column = 2)
multiplication.grid(row = 1, column = 3)
division.grid(row =1, column = 4)
power.grid(row = 1, column = 5)

one.grid(row = 2, column = 1)
two.grid(row = 2, column = 2)
three.grid(row = 2, column = 3)
four.grid(row = 2, column = 4)
five.grid(row = 2, column = 5)
six.grid(row = 2, column = 6)
seven.grid(row = 2, column = 7)
eight.grid(row = 2, column = 8)
nine.grid(row = 2, column = 9)                  


clear.grid(row = 3, column = 1,columnspan = 10)

    
root.mainloop()
