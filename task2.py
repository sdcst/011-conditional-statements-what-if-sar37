#! python3
"""
 Have the user input a number 
 Determine if the number is positive, negative or 0 
 2 points

 Inputs:
 number

 Outputs:
 - "positive"
 - "negative"
 - "zero"

 Example:

Enter a number: 3
positive

Enter a number: -1.2
negative
"""
question = "enter a number"
answer = input(question)
answer = float(answer)
x=0
if x>= 0:
    print("the number is positive")
if x< 0:
    print("the number is negative")
if x==0:
    print("the number is 0")
    