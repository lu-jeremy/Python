#14
print("Enter your year of birth.")
age=int(input())
print("Here's your age in years:",2017-age,".months:",(2017-age)*12,".weeks:",(2017-age)*52,".days:",(2017-age)*365,".minutes:",(2017-age)*525600,".and last but not least, seconds:",(2017-age)*31536000)
#Exercises15-16
print("What is your age?")
age=int(input())
if age>=16:
    print("You are eligible to drive.")
if age<16:
    print("You are not eligible to drive.")
    print("Sorry you can't drive yet. You will have to wait",16-age,"more years.")
#17
print("What is your gender and name?")
gender=input()
name=input()
if gender=="male":
    print("Hello Mr.",name)
if gender=="female":
    print("Hello Mrs.",name)
#18
print("Give me a number.")
number=int(input())
if number%2==0:
    print("Your number is an even number.")
else:
    print("Your number is an odd number.")
#18cont.
print("Give me your last test score in percentage, do not put  percentage sign at the end.")
number=int(input())
if 0<number<=59:
    print("You got an F for failure, shame on you.")
elif 60<number<=69:
    print("You got a D, D for dumb.")
elif 70<number<=79:
    print("You got a C, if you turn it to the right it becomes a frown face. It means you can't do anything RIGHT.")
elif 80<number<=89:
    print("You got a B, can I mention that B is for bad?")
elif 90<number<=100:
    print("You got an A! And guess what?! A is for average.")
else:
    print("Invalid Score, dumbo.")



