import tkinter
from tkinter import messagebox
root = tkinter.Tk()

root.title('5')

file = open("accounts.txt","r")

accounts = {}
#opening up file, reading every single line, then storing account inside file, so next time opening up the window will save the account
for var in file:
    #formatting of file is set to splitting by ':'
    u,p = var.split(':')
    accounts[u] = p[0:len(p)-1]
    print(accounts)
file.close()   
def l():
    if u_e.get() in accounts and p_e.get() == accounts[u_e.get()]:
        tkinter.messagebox.showinfo('MESSAGE', 'Login Successful')
    else:
        tkinter.messagebox.showinfo('MESSAGE', 'Login Failed, you need to create an account.')
        accounts[u_e.get()] = p_e.get()
        c()
        print(accounts)
def c():
    accounts[u_e.get()] = p_e.get()
    tkinter.messagebox.showinfo('MESSAGE','Create account successful')
    file = open("accounts.txt","w")
    for var in accounts:
        file.write(var+':'+accounts[var]+'\n')
    file.close()
        
username = tkinter.Label(root, text = 'Username')
password = tkinter.Label(root, text = 'Password')

login = tkinter.Button(root, text = 'Login', command = l)
create = tkinter.Button(root, text = 'Create an Account',command = c)


u_e = tkinter.Entry(root)
p_e = tkinter.Entry(root,show = '*')

username.grid(row = 0, column = 0)
u_e.grid(row = 0, column = 1)

password.grid(row = 1, column = 0)
p_e.grid(row = 1, column = 1)

login.grid(row = 3, column = 1)
create.grid(row = 3, column = 2)

 
root.mainloop()
