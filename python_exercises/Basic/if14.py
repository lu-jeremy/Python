print("What is your age?")
age=int(input())
if age>=16:
    print("You are eligible to drive.")
if age<16:
    print("You are not eligible to drive.")
    print("Sorry you can't drive yet. You will have to wait",16-age,"more years.")
print("What is your gender and name?")
gender=input()
name=input()
if gender=="male":
    print("Hello Mr.",name)
if gender=="female":
    print("Hello Mrs.",name)

        
