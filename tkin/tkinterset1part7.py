import tkinter
from tkinter import messagebox
import random

#images

root = tkinter.Tk()

root.title('3')
#root.geometry('400x400')
heads_img = tkinter.PhotoImage(file = "heads_coin.gif")
"""
panel = tkinter.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
"""

tails_img = tkinter.PhotoImage(file = "tails_coin.gif")
"""
panel = tkinter.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
"""
sides = ['Heads','Tails']
count = 0
score = 0
choice = random.choice(sides)

def t_choose():
    global choice
    global count
    global score
    tails = 'Tails'
    if choice == tails:
        tkinter.messagebox.showinfo('MESSAGE','You guessed RIGHT.')
        score +=1
        f_score['text'] = 'Score:'+str(score)
    else:
        tkinter.messagebox.showinfo('MESSAGE','You guessed WRONG.')
    tails = tkinter.Button(root,text = 'Tails')
    count+=1
    choice = random.choice(sides)
def h_choose():
    global count
    global choice
    global score
    heads = 'Heads'
    if choice == heads:
        tkinter.messagebox.showinfo('MESSAGE','You guessed RIGHT.')
        score += 1
        f_score['text'] = 'Score:'+str(score)
    else:
         tkinter.messagebox.showinfo('MESSAGE','You guessed WRONG.')
    heads = tkinter.Button(root,text = 'Heqds')       
    count+=1
    choice = random.choice(sides)

tails = tkinter.Button(root, image = tails_img,command = t_choose)
heads = tkinter.Button(root, image = heads_img, command = h_choose)
real_choice = tkinter.Label(root, text = '')
f_score = tkinter.Label(root, text = 'Score:%s'%score)

heads.grid(column = 0, row = 0)
tails.grid(column = 0, row = 1)
real_choice.grid(column = 1, row = 0)
f_score.grid(column = 2, row = 0)


while True:
    if count == 10:
        score = 0
        f_score['text'] = 'Score:%s'%score
    root.update()

root.mainloop()  
