import tkinter
#space invaders

class quiz():
    def __init__(self):
        self.root = tkinter.Tk()
        self.wait = 1
        self.score = 0
        self.questions = {
            'If the zero of a polynomial function is 3-2i, then \
what is for certain another answer to this function?':[['All of the \
above','Its conjugate', '3+2i', '(6+3i)-(3+i)'],['All of the above']],
'Write reasons why the soul is not real. Explain in detail.': [[],['soul','real','a']],
'Solve ln(e)':[['1', 'Undefined', 'e', 'I dont know'],['1']],
'Say whether it is moral to have people own autonomous vehicles in the future or not.':
[[],['moral','autonomous']],
'I am a chicken.':[['True','False'],['True']]
                                                                   }
    def next_question(self):
        print(question,self.questions[question][1])
        if len(self.questions[question][0]) >=2:
            for i in self.questions[question][0]:
                if i == self.questions[question][1][0]:
                    self.score+=1
            print(self.score)
        # first list is to see what kind of question it is (short answer, multiple choice, etc)
        # only add one point when all of the words in textbox in answers
        elif len(self.questions[question][0]) == 0:
            g = self.u_answer.get(0.0,tkinter.END)
            splitted = g.split()
            for a in self.questions[question][1]:
                print(splitted, a)
                if a in splitted:
                    self.score+=1
                    print(self.score)
        
        self.wait = 0
        self.q.grid_forget()
        self.frame.grid_forget()
        pass
    def run(self):
        global question
        self.one = tkinter.IntVar()
        self.two = tkinter.IntVar()
        self.three = tkinter.IntVar()
        self.four = tkinter.IntVar()
        for question in self.questions:
            self.wait = 1
            self.q = tkinter.Label(self.root, text = question)
            self.next_q = tkinter.Button(self.root, text = 'Next Question ->', command = self.next_question)
            self.frame = tkinter.Frame(self.root)
            #0 index is for the first element in the large list, and it also means that it will go to the first list because it is the first element
            if len(self.questions[question][0]) == 4:
               
                self.w_1 = tkinter.Checkbutton(self.frame,text = self.questions[question][0][0],onvalue = 1, offvalue = 0, var = self.one)
                self.w_2 = tkinter.Checkbutton(self.frame,text = self.questions[question][0][1],onvalue = 1, offvalue = 0, var = self.two)
                self.w_3 = tkinter.Checkbutton(self.frame,text = self.questions[question][0][2],onvalue = 1, offvalue = 0,var = self.three)
                self.correct = tkinter.Checkbutton(self.frame,text = self.questions[question][0][3],onvalue = 1, offvalue = 0,var = self.four)

                self.w_1.grid(row = 0, column = 0,sticky = 'W')
                self.w_2.grid(row = 1, column = 0,sticky = 'W')
                self.w_3.grid(row = 2, column = 0,sticky = 'W')
                self.correct.grid(row =3, column = 0, sticky = 'W')
            elif len(self.questions[question][0]) == 2:
                self.true = tkinter.Checkbutton(self.frame, text = self.questions[question][0][0], onvalue = 1, offvalue = 0)
                self.false = tkinter.Checkbutton(self.frame, text = self.questions[question][0][1], onvalue = 1, offvalue = 0)

                self.true.grid(row = 1, column = 0, sticky = 'W')
                self.false.grid(row = 2, column = 0, sticky = 'W')
            elif len(self.questions[question][0]) == 0:
                self.u_answer = tkinter.Text(self.frame)
                self.u_answer.grid(row = 0, column = 0)           
            self.q.grid(row = 0, column = 0)
            self.frame.grid(row = 1, column = 0)
            self.next_q.grid(row = 2, column = 0, sticky = 'E')

            while self.wait == 1:
                self.root.update()
        
        #self.root.mainloop()

r = quiz()
r.run()
