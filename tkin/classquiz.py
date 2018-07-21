import tkinter
# quiz of five, show results at end
class quiz():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('quiz')
        self.frame1 = tkinter.Frame(self.root)
        self.frame2 = tkinter.Frame(self.root)
        self.frame3 = tkinter.Frame(self.root)
        self.frame4 = tkinter.Frame(self.root)
        self.frame5 = tkinter.Frame(self.root)
        self.frame6 = tkinter.Frame(self.root)
        self.score = 0
        self.question_num = 1
        self.q1()
    def evaluation(self):
        if self.question_num ==1:
            if self.four.get() == 1:
                self.score+=1
            if self.one.get() == 1 and self.two.get() ==1 and self.three.get()==1:
                self.score+=1
            #forgetting frame will forget all of the other widgets in the frame
            self.frame1.grid_forget()
            print(self.score)
            self.q2()
        elif self.question_num==2:
            var = self.u_answer.get(1.0,tkinter.END)
            if 'soul' in var and 'study' in var and 'identity' in var and 'analogy' in var:
                self.score+=1
            self.frame2.grid_forget()
            self.q3()
        elif self.question_num ==3:
            if self.two.get() ==2:
                self.score+=1
            self.frame3.grid_forget()
            self.q4()
        elif self.question_num ==4:
            if self.entry.get() == 'Pneumonoultramicroscopicsilicovolcanoconiosis':
                self.score+=1
            self.frame4.grid_forget()
            self.q5()
        elif self.question_num ==5 :
            if self.entry.get() == '(-b +-√(b^2-4ac))/2a':
                self.score+=1
            self.frame5.grid_forget()
            self.result()
    def q2(self):
        self.question_num = 2
        self.question = tkinter.Message(self.frame2, width = 800,text = 'Write reasons why the soul is not real. Explain in detail.')
        self.u_answer = tkinter.Text(self.frame2)
        self.f_score = tkinter.Label(self.frame2, text = 'Score:%s'%self.score)
        self.next_q = tkinter.Button(self.frame2, text = 'Next Question ->', command = self.evaluation)
        
        self.next_q.grid(row = 5, column = 0,sticky = 'E')
        self.f_score.grid(row = 6, column = 0,sticky = 'E')
        self.question.grid(row = 0, column = 0)
        self.u_answer.grid(row = 1, column = 0)
        self.frame2.grid(row = 0, column = 0)
    def q3(self):
        self.question_num = 3
        self.question = tkinter.Message(self.frame3, bg = 'orange', width = 800, text = 'Pineapples grow on trees')
        self.true = tkinter.Checkbutton(self.frame3, text = 'True', onvalue = 2, offvalue = 1,variable = self.one)
        self.false = tkinter.Checkbutton(self.frame3, text = 'False', onvalue = 2, offvalue = 1, variable = self.two)
        self.next_q = tkinter.Button(self.frame3, text = 'Next Question ->',command = self.evaluation)
        self.f_score = tkinter.Label(self.frame3, text = 'Score:%s'%self.score)

        self.question.grid(row = 0, column = 0)
        self.true.grid(row = 1, column = 0, sticky = 'W')
        self.false.grid(row =2 , column = 0, sticky = 'W')
        self.next_q.grid(row = 3, column = 0, sticky = 'W')
        self.f_score.grid(row = 4, column = 0,sticky = 'E')
        self.frame3.grid(row =0, column = 0)
    def q4(self):
        self.question_num = 4
        self.question = tkinter.Message(self.frame4, width = 800, text = 'The longest word in the dictionary is')
        self.entry = tkinter.Entry(self.frame4)
        self.f_score = tkinter.Label(self.frame4, text = 'Score:%s'%self.score)
        self.next_q = tkinter.Button(self.frame4, text = 'Next Question ->', command = self.evaluation)

        self.question.grid(row = 0, column = 0, sticky = 'W')
        self.entry.grid(row = 0, column = 1, sticky = 'W')
        self.next_q.grid(row = 1, column = 0,sticky = 'W')
        self.f_score.grid(row = 2, column = 0,sticky = 'E')
        self.frame4.grid(row = 0, column = 0)
    def q5(self):
        self.question_num = 5
        self.question = tkinter.Message(self.frame5, width = 800, text = 'What is the Quadratic Formula?')
        self.entry = tkinter.Entry(self.frame5)
        self.f_score = tkinter.Label(self.frame5, text = 'Score:%s'%self.score)
        self.next_q = tkinter.Button(self.frame5, text = 'Next Question ->', command = self.evaluation)

        self.question.grid(row = 0, column = 0, sticky = 'W')
        self.entry.grid(row = 1, column = 0, sticky= 'W')
        self.f_score.grid(row = 3, column = 0, sticky = 'E')
        self.next_q.grid(row = 2, column = 0, sticky = 'W')
        self.frame5.grid(row = 0, column = 0)
    def result(self):
        self.question_num = 6
        self.question_one = tkinter.Message(self.frame6, width = 800, text = 'The answer to question one is: All of the above')
        self.question_two = tkinter.Message(self.frame6, width = 800, text = 'The answer to question two is correct if you included soul, identity, analogy, and study in your answer.')
        self.question_three = tkinter.Message(self.frame6, width = 800, text = 'The answer to question three is: False')
        self.question_four = tkinter.Message(self.frame6, width = 800, text = 'The answer to question four is: Pneumonoultramicroscopicsilicovolcanoconiosis')
        self.question_five = tkinter.Message(self.frame6, width = 800, text = 'The answer to question five is: (-b +-√(b^2-4ac))/2a')
        self.r = tkinter.Message(self.frame6, width = 800, text = 'And your final score is:%s'%self.score)

        self.question_one.grid(row = 0, column = 0, sticky = 'W')
        self.question_two.grid(row = 1, column = 0, sticky = 'W')
        self.question_three.grid(row = 2, column = 0, sticky = 'W')
        self.question_four.grid(row = 3, column = 0, sticky = 'W')
        self.question_five.grid(row = 4, column = 0, sticky = 'W')
        self.r.grid(row =5, column = 0, sticky = 'W')
        self.frame6.grid(row = 0, column = 0)
    def q1(self):
        self.one = tkinter.IntVar()
        self.two = tkinter.IntVar()
        self.three = tkinter.IntVar()
        self.four = tkinter.IntVar()
        self.multiple_choice = tkinter.Message(self.frame1,bg = 'yellow',width = 800,text = 'If the zero of a polynomial function is 3-2i, then what is for certain another answer to this function?')
        self.w_1 = tkinter.Checkbutton(self.frame1,text = '3+2i',onvalue = 1, offvalue = 0,variable = self.one)
        self.w_2 = tkinter.Checkbutton(self.frame1,text = 'Its conjugate',onvalue = 1, offvalue = 0,variable = self.two)
        self.w_3 = tkinter.Checkbutton(self.frame1,text = '(6+3i)-(3+i)',onvalue = 1, offvalue = 0, variable = self.three)
        self.correct = tkinter.Checkbutton(self.frame1,text = 'All of the above',onvalue = 1, offvalue = 0, variable = self.four)
        self.next_q = tkinter.Button(self.frame1, text = 'Next Question ->',command = self.evaluation)
        self.f_score = tkinter.Label(self.frame1,text = 'Score:%s'%self.score)

        self.multiple_choice.grid(row = 0, column = 0)
        self.w_1.grid(row = 1, column = 0,sticky = 'W')
        self.w_2.grid(row = 2, column = 0,sticky = 'W')
        self.w_3.grid(row = 3, column = 0,sticky = 'W')
        self.correct.grid(row = 4, column = 0,sticky = 'W')
        self.next_q.grid(row = 5, column = 0,sticky = 'E')
        self.f_score.grid(row = 6, column = 0, sticky = 'E')
        self.frame1.grid(row = 0, column = 0)
    def run(self):
        self.root.mainloop()

q = quiz()
q.run()
