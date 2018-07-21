import tkinter
import time

global score 
root = tkinter.Tk()
score = 0

def thing():
    global score
    global f_score
    get1 = int(one_e.get())
    get2 = int(two_e.get())
    get3 = int(three_e.get())
    get4 = int(four_e.get())
    get5 = int(five_e.get())
    if get1 == 0:
        score += 1
    if get2 == 2:
        score += 1
    if get3 == 25:
        score +=1
    if get4 == 1:
        score += 1
    if get5 == 4:
        score += 1
    print(score)
    f_score['text'] = 'Score:%s'%score
    score = 0
def reset_fx():
    one_e.delete(0,tkinter.END)
    two_e.delete(0,tkinter.END)
    three_e.delete(0,tkinter.END)
    four_e.delete(0,tkinter.END)
    five_e.delete(0,tkinter.END)

submit = tkinter.Button(root, text = 'Submit',command = thing)
reset = tkinter.Button(root, text = 'Reset',command = reset_fx)
leave = tkinter.Button(root, text = 'Quit',command = exit)
question_one = tkinter.Label(root, text = 'How much wood would a wood chuck chuck if a wood chuck could chuck wood?')
question_two = tkinter.Label(root, text = '1+1')
question_three = tkinter.Label(root, text = '5x5')
question_four = tkinter.Label(root, text = 'tan45')
question_five = tkinter.Label(root , text = '2+2')
f_score = tkinter.Label(root , text = 'Score:%s'%score)



one_e = tkinter.Entry(root)
two_e = tkinter.Entry(root)
three_e = tkinter.Entry(root)
four_e = tkinter.Entry(root)
five_e = tkinter.Entry(root)

question_one.grid(row = 0, column = 0)
one_e.grid(row = 0, column = 1)

question_two.grid(row = 1, column = 0)
two_e.grid(row = 1, column = 1)

question_three.grid(row = 2, column = 0)
three_e.grid(row = 2, column = 1)

question_four.grid(row = 3, column = 0)
four_e.grid(row = 3, column = 1)

question_five.grid(row = 4, column = 0)
five_e.grid(row = 4, column = 1)

submit.grid(row = 5, column = 0)
reset.grid(row = 5, column = 1)
leave.grid(row = 5, column = 2)
f_score.grid(row = 5, column = 3)

root.title('2')
root.mainloop()
