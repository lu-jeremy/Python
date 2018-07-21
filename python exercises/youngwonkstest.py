import random
headsortails=['heads','tails']
usercoinpicks=[]
computercoinpicks=[]
attempts=0
score=0
end=0
while end==0:
    print('Give me a game you want to play, coin toss or number guessing game?')
    choice=input()
    if choice=='coin toss':
        print('Great choice! Now choose a coin side')
        while attempts<=10:
            side=input()
            usercoinpicks.append(side)
            headsortailschoice=random.choice(headsortails)
            computercoinpicks.append(headsortailschoice)
            if side==headsortailschoice:
                print('You got it right')
                attempts=attempts+1
                score=score+1
            else:
                print('You got it wrong')
                attempts=attempts+1
        end=end+1
        print('Great! Now here is your score:',score,'/10')
        print('Here is your inputs:', usercoinpicks, 'Here is the computer inputs:', computercoinpicks)
    elif choice=='number guessing game':
        computernum=random.randint(1,15)
        numberguessesforuser=[]
        print(computernum)
        print('Press a key to continue.')
        numberguess=input()
        while numberguess!=computernum:
            print('Guess a number')
            numberguess=int(input())
            print(numberguess)
            if numberguess==computernum:
                print('Great job. You guessed the number.')
                print(numberguessesforuser,'this is your guesses')
                print('this is the correct answer:',computernum)
                numberguessesforuser.append(numberguess)
            if numberguess!=computernum:
                print('Try again.')
                numberguessesforuser.append(numberguess)
        end=end+1
    else:
        print('Please choose coin toss or number guessing game.')
