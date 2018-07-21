import tkinter
import time



var = 0
stop = 0

def count_down():
    global var
    global stop
    stop = 0
    amount = int(a_duration.get())
    var = amount
    while stop == 0 and var > 0:
        time.sleep(1)
        f['text'] = var
        var = var - 1
        root.update()
        
def Reset():
    global stop
    stop = 1
    var = 0
    f['text'] = var
    
#1
root = tkinter.Tk()

start = tkinter.Button(root, text = 'Start', command = count_down )

reset = tkinter.Button(root, text = 'Reset',command = Reset)


f = tkinter.Label(root, text = var)

                             
a_duration = tkinter.Entry(root)

start.pack(side = tkinter.LEFT)
reset.pack(side = tkinter.LEFT)
a_duration.pack(side = tkinter.RIGHT)
f.pack(side = tkinter.RIGHT)



#2
root.title('1')

#3
root.mainloop()
