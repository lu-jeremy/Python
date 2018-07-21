import tkinter
from tkinter import messagebox
root = tkinter.Tk()

def thing():
    global score
    global f_score
    global answer
    answer = 1
    answer = int(entry.get())
    if answer == int(d[question['text']]):
        score += 1
        tkinter.messagebox.showinfo('MESSAGE','Correct answer')
    else:
        tkinter.messagebox.showinfo('MESSAGE','Wrong answer')
    entry.delete(0,tkinter.END)
    print(score)
    f_score['text'] = 'Score:%s'%score
    return
d = {'How much wood would a wood chuck chuck if a wood chuck could chuck wood?': 0,
     '1+1':2,
     '5x5':25,
     'tan45':1,
     '2+2':4}
answer = None
score = 0
question = tkinter.Label(root, text = '')
entry = tkinter.Entry(root)
submit = tkinter.Button(root, text = 'Submit', command = thing)
reset = tkinter.Button(root, text = 'Reset')
leave = tkinter.Button(root, text = 'Quit',command = exit)
f_score = tkinter.Label(root , text = 'Score:%s'%score)

question.grid(row = 0, column = 0)
entry.grid(row = 0, column = 1)
submit.grid(row = 1, column = 0)
reset.grid(row = 1, column = 1)
leave.grid(row = 1,column = 2)
f_score.grid(row = 1, column = 3)

for var in d:
    question['text'] = var
    print(var)
    root.update()
    while answer!=d[question['text']]:
        root.update()
score = 0
exit()
"""

        
def reset_fx():
    one_e.delete(0,tkinter.END)
def q2():
    question_one.grid_forget()
    one_e.grid_forget()
    question_two.grid(row = 0, column = 0)
    two_e.grid(row = 0, column = 1)
def q3():
    question_two.grid_forget()
    two_e.grid_forget()
    question_three.grid(row = 0, column = 0)
    three_e.grid(row = 0, column = 1)
    
#q
question_one = tkinter.Label(root, text = 'How much wood would a wood chuck chuck if a wood chuck could chuck wood?')
question_two = tkinter.Label(root, text = '1+1')
question_three = tkinter.Label(root, text = '5x5')
question_four = tkinter.Label(root, text = 'tan45')
question_five = tkinter.Label(root , text = '2+2')
f_score = tkinter.Label(root , text = 'Score:%s'%score)

#b
submit = tkinter.Button(root, text = 'Submit',command = thing)
reset = tkinter.Button(root, text = 'Reset',command = reset_fx)
leave = tkinter.Button(root, text = 'Quit',command = exit)

#e
e = tkinter.Entry(root)


#q1
question_one.grid(row = 0, column = 0)
one_e.grid(row = 0, column = 1)
submit.grid(row = 1, column = 0)
reset.grid(row = 1, column = 1)
leave.grid(row = 1, column = 2)
f_score.grid(row = 1, column = 3)
"""

root.title('2')
root.mainloop()

