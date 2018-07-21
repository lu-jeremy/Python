import tkinter
import random
from tkinter import messagebox

#number guessing game
root = tkinter.Tk()
root.title('3')
score = 0
rannum = random.randint(0,10)
print(rannum)
def thing():
    global rannum
    global score
    print(rannum)
    get1 = int(e1.get())
    e1.delete(0,tkinter.END)
    if get1 == rannum:
        tkinter.messagebox.showinfo('MESSAGE','You guessed right')
        rannum = random.randint(0,10)
        score = 0
        f_score['text'] = 'Score:%s'%score
    else:
        tkinter.messagebox.showinfo('MESSAGE','You guessed WRONG')
        score += 1
        f_score['text'] = 'Score:%s'%score
#tkinter.messagebox.showinfo('MESSAGE','Enter a number from 1-10')


number = tkinter.Label(root, text = 'Enter a number from 1-10:')

e1 = tkinter.Entry(root)

submit = tkinter.Button(root, text = 'Submit',command = thing)
f_score = tkinter.Label(root,text = 'Score:%s'%score)

number.grid(column = 0, row = 0)
e1.grid(column = 0, row = 1)
submit.grid(column = 1, row = 0)
f_score.grid(column = 1, row = 1)

while True:
    root.update()


root.mainloop()
