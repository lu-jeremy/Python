import random
"""
#quiz
score=0
asking=0
questionswithvalues = {"If you were born an empty soul, would you NOT do the exact same actions as somebody else if you were born that person?":"no",
                       "What is 8n=12*4, solving for n(decimal form)?":"n=6.",
                       "Is it possible for the sun to be in the middle of the Earth and moon?": "no",
                       "Does a summary include a writer's own opinion about an article, video, etc.?":"no",
                       "Is walking considered an anaerobic activity?": "yes",
                       "What does S.T.E.M stand for?(left to right)": "science, technology, engineering, math",
                       "What is viente seis in English?(give me a number)": "26",
                       "What is the formula of the surface area of a cylinder?(write pi and ^2)":"2pirh+2pir^2",
                       "How many letters are in the English alphabet?":"26",
                       "Write a word.":"a word"}

while asking<5 and score<6:
    pick=random.choice(list(questionswithvalues))
    print("Answer the following question:")
    print("")
    print(pick)
    answer=input()
    if answer==questionswithvalues[pick]:
        print("You got the answer correct.")
        print("Real answer:",questionswithvalues[pick])
        score=score+1
        print("You gained a point. Score:",score)
    else:
        asking=asking+1
        score=score-1
        print("You got the answer wrong.")
        print("Real answer:",questionswithvalues[pick])
        print("You deducted a point. Score:",score)
print("Sorry, you do not have any more tries.")
"""




#TicTacToe
numbers = {1:"_", 2:"_",3:"_",
           4:"_",5:"_",6:"_",7:"_",8:"_",9:"_"}
#definition of tictactoe, easier to call later
def tictactoe():
    print(numbers[1],numbers[2],numbers[3])
    print(numbers[4],numbers[5],numbers[6])
    print(numbers[7],numbers[8],numbers[9])
while True:
    #calling tictactoe
    tictactoe()
    print("Give me a number between 1 and 9.");
    #asking for input
    NID=int(input())
    #if the NID index numbers value is not correct
    while numbers[NID]!="_":
        print("Give me another number.")
        #input new number
        NID=int(input())
    #value of NID is x 
    numbers[NID]="x"
    #combinations
    if numbers[1]==numbers[2]==numbers[3]=="x" or numbers[1]==numbers[4]==numbers[7]=="x" or numbers[2]==numbers[5]==numbers==[8]=="x" or numbers[3]==numbers[6]==numbers[9]=="x" or numbers[4]==numbers[5]==numbers[6]=="x" or numbers[7]==numbers[8]==numbers[9]=="x" or numbers[1]==numbers[5]==numbers[9]=="x" or numbers[3]==numbers[5]==numbers[7]=="x":
        print("Player x has won!")
        #calls tictactoe in order to print out the winning tictactoe grid
        tictactoe()
        print("Game restart.")
        #restarts the game by printing out the dictionary and can input anything back into it; clears it
        numbers = {1:"_", 2:"_",3:"_",
           4:"_",5:"_",6:"_",7:"_",8:"_",9:"_"}
        #for o, chooses random integer
    randomchoice=random.randint(1,9)
    #if the value of randomchoice is not "_" then choose a new number
    while numbers[randomchoice]!="_":
        randomchoice=random.randint(1,9)
        #value of randomchoice is o
    numbers[randomchoice]="o"
    if numbers[1]==numbers[2]==numbers[3]=="o" or numbers[1]==numbers[4]==numbers[7]=="o" or numbers[2]==numbers[5]==numbers==[8]=="o" or numbers[3]==numbers[6]==numbers[9]=="o" or numbers[4]==numbers[5]==numbers[6]=="o" or numbers[7]==numbers[8]==numbers[9]=="o" or numbers[1]==numbers[5]==numbers[9]=="o" or numbers[3]==numbers[5]==numbers[7]=="o":
        print("Player o has won!")
        #calls tictactoe in order to print out the winning tictactoe grid
        tictactoe()
        print("Game restart.")
        numbers = {1:"_", 2:"_",3:"_",
           4:"_",5:"_",6:"_",7:"_",8:"_",9:"_"}
        #if all of the numbers are filled
    if "_" not in numbers.values():
        print("Do you want to restart the game? Yes or No?")
        response=input()
        if not (response=="yes"):
            numbers = {1:"_", 2:"_",3:"_",
           4:"_",5:"_",6:"_",7:"_",8:"_",9:"_"}
            
