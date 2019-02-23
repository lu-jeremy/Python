import tkinter as tk
from tkinter import *
from tkinter.font import Font
import sys

#PLEASE PRESS THE PLAY BUTTON ON THE TOP RIGHT TO RUN THE PROGRAM

class Questions:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('13 Colonies/Colonial Life Trivia')
        self.short_answer = []
        self.question_number = 0
        self.score = 0
        self.one = tk.IntVar()
        self.two = tk.IntVar()
        self.three = tk.IntVar()
        self.four = tk.IntVar()
        self.q1()
    def evaluation(self):
        if self.question_number == 1:
            key_words = ['Puritans', 'Separatists', 'May Flower Compact', 'charter']
            for word in key_words:
                if word in self.input.get(1.0, tk.END):
                    self.score += 0.25
            self.frame_one.grid_forget()
            self.q2()
        elif self.question_number == 2:
            key_words = ['founded', 'Pennsylvania', 'Quakers']
            for word in key_words:
                if word in self.input.get(1.0, tk.END):
                    self.score += 0.5
            self.frame_two.grid_forget()
            self.q3()
        elif self.question_number == 3:
            if self.one.get() == 1:
                self.score += 1
            self.frame_three.grid_forget()
            self.q4()
        elif self.question_number == 4:
            if self.one.get() == 1:
                self.score += 0.5
            if self.four.get() == 1:
                self.score += 0.5
            self.frame_four.grid_forget()
            self.q5()
        elif self.question_number == 5:
            if self.two.get() == 1:
                self.score += 1
            self.frame_five.grid_forget()
            self.q6()
        elif self.question_number == 6:
            if self.three.get() == 1:
                self.score += 0.5
            if self.four.get() == 1:
                self.score += 0.5
            self.frame_six.grid_forget()
            self.q7()
        elif self.question_number == 7:
            if self.slider.get() == 1619:
                self.score += 1
            self.frame_seven.grid_forget()
            self.q8()
        elif self.question_number == 8:
            if self.slider.get() == 1661:
                self.score +=1 
            self.frame_eight.grid_forget()
            self.q9()
        elif self.question_number == 9:
            if 15000 <= self.slider.get() <= 17000:
                self.score += 1
            self.frame_nine.grid_forget()
            self.q10()
        elif self.question_number == 10:
            if self.four.get() == 1:
                self.score += 1
            self.frame_ten.grid_forget()
            self.q11()
        elif self.question_number == 11:
            if self.three.get() == 1:
                self.score += 1
            if self.four.get() == 1:
                self.score +=1
            self.frame_eleven.grid_forget()
            self.q12()
        elif self.question_number == 12:
            if self.four.get() == 1:
                self.score += 1
            self.frame_twelve.grid_forget()
            self.q13()
        elif self.question_number == 13:
            if self.one.get() == 1:
                self.score += 1
            self.frame_thirteen.grid_forget()
            self.final_screen()        
    def q1(self):
        self.question_number = 1
        self.frame_one = tk.Frame(self.root)
        self.question = tk.Message(self.frame_one, bg = 'green', text = 'How was Massachusetts founded?', width = 800)
        self.input = tk.Text(self.frame_one, bg = 'salmon1')
        self.next_question = tk.Button(self.frame_one, text = 'Next Question ->', command = self.evaluation)

        self.frame_one.grid(row = 0, column = 0)
        self.question.grid(row = 0, column = 0, sticky = 'W')
        self.input.grid(row = 1, column = 0)
        self.next_question.grid(row = 2, column = 0, sticky = 'E')
    def q2(self):
        self.question_number = 2
        self.frame_two = tk.Frame(self.root)
        self.question = tk.Message(self.frame_two, bg = 'SeaGreen1', text = 'Who was William Penn?', width = 800)
        self.input = tk.Text(self.frame_two, bg = 'gold')
        self.next_question = tk.Button(self.frame_two, text = 'Next Question ->', command = self.evaluation)

        self.frame_two.grid(row = 0, column = 0)
        self.question.grid(row = 0, column = 0, sticky = 'W')
        self.input.grid(row = 1, column = 0)
        self.next_question.grid(row = 2, column = 0, sticky = 'E')    
    def q3(self):
        self.question_number = 3
        self.frame_three = tk.Frame(self.root)
        self.question = tk.Message(self.frame_three, width = 800, bg = 'steel blue', text = 'What is the capital '
                                                                    'city of Pennsylvania?')
        self.correct = tk.Checkbutton(self.frame_three, bg = 'SkyBlue1', width = 100, text = 'Philadelphia',onvalue = 1, 
                                                            offvalue = 0, variable = self.one)
        self.option_two = tk.Checkbutton(self.frame_three, bg = 'SkyBlue2', width = 100, text = 'Des Moines', onvalue = 1, 
                                                            offvalue = 0, variable = self.two)
        self.option_three = tk.Checkbutton(self.frame_three, bg = 'SkyBlue3', width = 100, text = 'There was none at the time', 
                                                            onvalue = 1, offvalue = 0, 
                                                            variable = self.three)
        self.option_four = tk.Checkbutton(self.frame_three, bg = 'SkyBlue4', width = 100, text = 'Austin', onvalue = 1, 
                                                            offvalue = 0, variable = self.four)
        self.next_question = tk.Button(self.frame_three, text = 'Next Question ->', command = self.evaluation)
        
        self.frame_three.grid(row = 0, column = 0)
        self.question.grid(row = 0, column = 0)
        self.correct.grid(row = 1, column = 0)
        self.option_two.grid(row = 2, column = 0)
        self.option_three.grid(row = 3, column = 0)
        self.option_four.grid(row = 4, column = 0)
        self.next_question.grid(row = 5, column = 0, sticky = 'E')
    def q4(self):
        self.question_number = 4
        self.frame_four = tk.Frame(self.root)
        self.question = tk.Message(self.frame_four, width = 800, bg = 'RoyalBlue1', text = 'After The Act of Concerning Religion in Maryland was passed, '
                                            '_______ of America at the time, '
                                            'the Protestants and Catholics were still _______ of each other. (MA)')
        self.correct_one = tk.Checkbutton(self.frame_four, bg = 'CadetBlue1', width = 100, 
                                                                    text = 'first law', onvalue = 1, 
                                                                    offvalue = 0, variable = self.one)
        self.option_two = tk.Checkbutton(self.frame_four, bg = 'CadetBlue2', width = 100, 
                                                                    text = 'church rule', onvalue = 1,
                                                                    offvalue = 0, variable = self.two)
        self.option_three = tk.Checkbutton(self.frame_four, bg = 'CadetBlue3', width = 100, 
                                                                    text = 'disfavoring', onvalue = 1,
                                                                    offvalue = 0, variable = self.three)
        self.correct_four = tk.Checkbutton(self.frame_four, bg = 'CadetBlue4', width = 100, 
                                                                    text = 'suspicious', onvalue = 1,
                                                                    offvalue = 0, variable = self.four)
        self.next_question = tk.Button(self.frame_four, text = 'Next Question ->', 
                                                        command = self.evaluation)

        self.frame_four.grid(row = 0, column = 0)
        self.question.grid(row = 0, column = 0)
        self.correct_one.grid(row = 1, column = 0)
        self.option_two.grid(row = 2, column = 0)
        self.option_three.grid(row = 3, column = 0)
        self.correct_four.grid(row = 4, column = 0)
        self.next_question.grid(row = 5, column = 0, sticky = 'E')
    def q5(self):
        self.question_number = 5
        self.frame_five = tk.Frame(self.root)
        self.question = tk.Message(self.frame_five, width = 800, bg = 'aquamarine', 
                                                    text = 'What was Virginia\'s '
                                                    'main cash crop?')
        self.option_one = tk.Checkbutton(self.frame_five, width = 100, bg = 'RoyalBlue1', text = 'rice',
                                                    onvalue = 1, offvalue = 0, variable = self.one)
        self.correct = tk.Checkbutton(self.frame_five, width = 100, bg = 'RoyalBlue2', text = 'tobacco',
                                                    onvalue = 1, offvalue = 0, variable = self.two)
        self.option_three = tk.Checkbutton(self.frame_five, width = 100, bg = 'RoyalBlue3', text = 'corn',
                                                    onvalue = 1, offvalue = 0, variable = self.three)
        self.option_four = tk.Checkbutton(self.frame_five, width = 100, bg = 'RoyalBlue4', text = 'cotton',
                                                    onvalue = 1, offvalue = 0, variable = self.four)
        self.next_question = tk.Button(self.frame_five, text = 'Next Question ->',
                                                        command = self.evaluation)
        self.frame_five.grid(row = 0, column = 0)
        self.question.grid(row = 0, column = 0)
        self.option_one.grid(row = 1, column = 0)
        self.correct.grid(row = 2, column = 0)
        self.option_three.grid(row = 3, column = 0)
        self.option_four.grid(row = 4, column = 0)
        self.next_question.grid(row = 5, column = 0, sticky = 'E')
    def q6(self):
        self.question_number = 6
        self.frame_six = tk.Frame(self.root)
        self.question = tk.Message(self.frame_six, width = 800, bg = 'cadet blue', text = 'Why did the colonists think '
                                            'that Africans were most suitable to be slaves? (MA)')
        self.option_one = tk.Checkbutton(self.frame_six, width = 100, bg = 'SeaGreen1', text = 'they weren\'nt',
                                                    onvalue = 1, offvalue = 0, variable = self.one)
        self.option_two = tk.Checkbutton(self.frame_six, width = 100, bg = 'SpringGreen2', text = 'they were the friendliest',
                                                    onvalue = 1, offvalue = 0, variable = self.two)
        self.correct_three = tk.Checkbutton(self.frame_six, width = 100, bg = 'SpringGreen3', text = 'they were used to work',
                                                    onvalue = 1, offvalue = 0, variable = self.three)  
        self.correct_four = tk.Checkbutton(self.frame_six, width = 100, bg = 'SpringGreen4', text = 'dark skin did '
                    'not blend in with the crowd', onvalue = 1, offvalue = 0, variable = self.four)
        self.next_question = tk.Button(self.frame_six, text = 'Next Question ->', 
                                                        command = self.evaluation)

        self.frame_six.grid(row = 0, column = 0)
        self.question.grid(row = 0, column = 0)
        self.option_one.grid(row = 1, column = 0)
        self.option_two.grid(row = 2, column = 0)
        self.correct_three.grid(row = 3, column = 0)
        self.correct_four.grid(row = 4, column = 0)
        self.next_question.grid(row = 5, column = 0, sticky = 'E')
    def run(self):
        self.root.mainloop()
    def q7(self):
        self.question_number = 7
        self.frame_seven = tk.Frame(self.root)
        self.question = tk.Message(self.frame_seven, width = 800, bg = 'papaya whip', text = 'When did Virginia '
                                                                        'elect a House of Burgesses?')
        self.slider = tk.Scale(self.frame_seven, length = 600, from_ = 1200, to = 1800, orient = HORIZONTAL)
        self.next_question = tk.Button(self.frame_seven, text = 'Next Question ->', command = self.evaluation)

        self.frame_seven.grid(row = 0, column = 0)
        self.question.grid(row = 0, column = 0)
        self.slider.grid(row = 1, column = 0)
        self.next_question.grid(row = 2, column = 0, sticky = 'E')
    def q8(self):
        self.question_number = 8
        self.frame_eight = tk.Frame(self.root)
        self.question = tk.Message(self.frame_eight, width = 800, bg = 'gray64', text = 'When did Virginia '
                                                            'have African workers slaves for life?')
        self.slider = tk.Scale(self.frame_eight, length = 600, from_ = 1200, to = 1800, orient = HORIZONTAL)
        self.next_question = tk.Button(self.frame_eight, text = 'Next Question ->', command = self.evaluation)
        
        self.frame_eight.grid(row = 0, column = 0)
        self.question.grid(row = 0, column = 0)
        self.slider.grid(row = 1, column = 0)
        self.next_question.grid(row = 2, column = 0, sticky = 'E')
    def q9(self):
        self.question_number = 9
        self.frame_nine = tk.Frame(self.root)
        self.question = tk.Message(self.frame_nine, width = 800, bg = 'hot pink', text = 'About how many slaves '
                                                                    'were there by the 1700s in Virginia? (answer doesn\'t need to be exact')
        self.slider = tk.Scale(self.frame_nine, length = 600, from_ = 10000, to = 22000, orient = HORIZONTAL)
        self.next_question = tk.Button(self.frame_nine, text = 'Next Question ->', command = self.evaluation)

        self.frame_nine.grid(row = 0, column = 0)
        self.question.grid(row = 0, column = 0)
        self.slider.grid(row = 1, column = 0)
        self.next_question.grid(row = 2, column = 0, sticky = 'E')
    def q10(self):
        self.question_number = 10
        self.frame_ten = tk.Frame(self.root)
        self.question = tk.Message(self.frame_ten, width = 800, bg = 'brown4', text = 'What was the Magna Carta?')
        self.option_one = tk.Checkbutton(self.frame_ten, bg = 'DarkOrange1', width = 100, text = 'a list of rights for the citizens',
                                                    onvalue = 1, offvalue = 0, variable = self.one)
        self.option_two = tk.Checkbutton(self.frame_ten, bg = 'DarkOrange2', width = 100, text = 'a document with how the government will be set up',
                                                    onvalue = 1, offvalue = 0, variable = self.two)
        self.option_three = tk.Checkbutton(self.frame_ten, bg = 'DarkOrange3', width = 100, text = 'a rule that people must go to church on Sunday')
        self.correct = tk.Checkbutton(self.frame_ten, bg = 'DarkOrange4', width = 100, text = 'an agreement that limited monarch\'s power',
                                                    onvalue = 1, offvalue = 0, variable = self.four)
        self.next_question = tk.Button(self.frame_ten, text = 'Next Question ->', command = self.evaluation)
  
        self.frame_ten.grid(row = 0, column = 0)
        self.question.grid(row = 0, column = 0)
        self.option_one.grid(row = 1, column = 0)
        self.option_two.grid(row = 2, column = 0)
        self.option_three.grid(row = 3, column = 0)
        self.correct.grid(row = 4, column = 0)
        self.next_question.grid(row = 5, column = 0, sticky = 'E')
    def q11(self):
        self.question_number = 11
        self.frame_eleven = tk.Frame(self.root)
        self.question = tk.Message(self.frame_eleven, width = 800, bg = 'rosy brown', text = 'What was English Bill of Rights? (MA)')
        self.option_one = tk.Checkbutton(self.frame_eleven, width = 100, bg = 'honeydew2', text = 'the great charter',
                                                        onvalue = 1, offvalue = 0, variable = self.one)
        self.option_two = tk.Checkbutton(self.frame_eleven, width = 100, bg = 'honeydew3', text = 'a respectful letter to the king',
                                                        onvalue = 1, offvalue = 0, variable = self.two)
        self.correct_three = tk.Checkbutton(self.frame_eleven, width = 100, bg = 'honeydew4', text = 'a list of rights belonging to the people',
                                                        onvalue = 1, offvalue = 0, variable = self.three)
        self.correct_four = tk.Checkbutton(self.frame_eleven, width = 100, bg = 'ivory4', text = 'increased power in Parliament',
                                                        onvalue = 1, offvalue = 0, variable = self.four)
        self.next_question = tk.Button(self.frame_eleven, text = 'Next Question ->', command = self.evaluation)

        self.frame_eleven.grid(row = 0, column = 0)
        self.question.grid(row = 0, column = 0)
        self.option_one.grid(row = 1, column = 0)
        self.option_two.grid(row = 2, column = 0)
        self.correct_three.grid(row = 3, column = 0)
        self.correct_four.grid(row = 4, column = 0)
        self.next_question.grid(row = 5, column = 0, sticky = 'E')
    def q12(self):
        self.question_number = 12
        self.frame_twelve = tk.Frame(self.root)
        self.question = tk.Message(self.frame_twelve, width = 800, bg = 'cornflower blue', text = 'What is the Sabbath?')
        self.option_one = tk.Checkbutton(self.frame_twelve, width = 100, bg = 'dark slate blue', text = 'a rule for slaves',
                                                        onvalue = 1, offvalue = 0, variable = self.one)
        self.option_two = tk.Checkbutton(self.frame_twelve, width = 100, bg = 'slate blue', text = 'a rule for ports',
                                                        onvalue = 1, offvalue = 0, variable = self.two)
        self.option_three = tk.Checkbutton(self.frame_twelve, width = 100, bg = 'medium slate blue', text = 'a rule for basic rights of citizens',
                                                        onvalue = 1, offvalue = 0, variable = self.three)
        self.correct_four = tk.Checkbutton(self.frame_twelve, width = 100, bg = 'light slate blue', text = 'a rule by church that states people cannot work or travel on Sunday',
                                                        onvalue = 1, offvalue = 0, variable = self.four)
        self.next_question = tk.Button(self.frame_twelve, text = 'Next Question ->', command = self.evaluation)

        self.frame_twelve.grid(row = 0, column = 0)
        self.question.grid(row = 0, column = 0)
        self.option_one.grid(row = 1, column = 0)
        self.option_two.grid(row = 2, column = 0)
        self.option_three.grid(row = 3, column = 0)
        self.correct_four.grid(row = 4, column = 0)
        self.next_question.grid(row = 5, column = 0, sticky = 'E')
    def q13(self):
        self.question_number = 13
        self.frame_thirteen = tk.Frame(self.root)
        self.question = tk.Message(self.frame_thirteen, bg = 'thistle1', width = 800, text = 'People will get a death penalty in those days if they curse or strike their parents.')
        self.true = tk.Checkbutton(self.frame_thirteen, bg = 'sea green', width = 100, text = 'True', onvalue = 1, offvalue = 0, variable = self.one)
        self.false = tk.Checkbutton(self.frame_thirteen, bg = 'medium sea green', width = 100, text = 'False', onvalue = 1, offvalue = 0, variable = self.two)
        self.next_question = tk.Button(self.frame_thirteen, text = 'Next Question ->', command = self.evaluation)

        self.frame_thirteen.grid(row = 0, column = 0)
        self.question.grid(row = 0, column = 0)
        self.true.grid(row = 1, column = 0)
        self.false.grid(row = 2, column = 0)
        self.next_question.grid(row = 3, column = 0, sticky = 'E')
    def final_screen(self):
        self.question_number = 14
        self.frame_fourteen = tk.Frame(self.root)
        self.message = tk.Message(self.frame_fourteen, width = 800, text = 'Well done! You got through the quiz that took me 3 hours to make! Now I\'m so burnt out from making this that I can\'t even add a background color to this frame. Yay!')
        self.score = tk.Label(self.frame_fourteen, text = 'Score: %s'%self.score)
        self.exit = tk.Button(self.frame_fourteen, text = 'Exit ->', command = sys.exit)

        self.frame_fourteen.grid(row = 0, column = 0)
        self.message.grid(row = 0, column = 0)
        self.score.grid(row = 1, column = 0)
        self.exit.grid(row = 2, column = 0, sticky = 'E')
class Trivia:
    def __init__(self):
        self.root = tk.Tk()
        self.frame_start = tk.Frame(self.root)
        self.bold_font = Font(family="Helvetica", size=14, weight="bold")
        self.start_screen()
    def update_questions(self):
        self.q = Questions()
        self.q.run()
    def start_screen(self):
        self.root.title('Starting Screen')
        self.intro = tk.Message(self.frame_start, font = self.bold_font, width = 800, bg = 'green', text = 'Hello there! Welcome to my trivia, '
                            'my name is Jeremy Lu and I hope you get 100% on this trivia which you '
                            'should probably pass mostly because you learned all of this material already. '
                            'If it says (MA) next to the question it means there are multiple answers. '
                            'You can get rid of this window after starting the trivia, and remember '
                            'that you cannot go back after you answered a question. Good Luck!')
        self.start_trivia = tk.Button(self.frame_start, text = 'Start Trivia', command = self.update_questions)
        self.quit = tk.Button(self.frame_start, text = 'Quit Trivia', command = sys.exit)
        
        self.intro.grid(row = 0, column = 0)
        self.start_trivia.grid(row = 1, column = 0)
        self.quit.grid(row = 3, column = 0, sticky = 'E')
        self.frame_start.grid(row = 0, column = 0)
    def run(self):
        self.root.mainloop()

Trivia().run()