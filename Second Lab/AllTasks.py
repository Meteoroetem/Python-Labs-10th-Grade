def Introduction():
    heigh=float(input("Enter your height\n"))
    if ( heigh>1.6 ):
        print("You are in a basketball team!!")
    else:
        print ("You are in a football team!!")
    '''
    Output:
    1.7: You are in a basketball team!!
    1.8: You are in a basketball team!!
    1.5: You are in a football team!!
    '''

def Introduction2():
    print(" welcome to Python Class!!")
    name = input (" what is your name?!!")
    print(name, " -is a beautiful name!!")
    heigh=float(input("Enter your height\n"))
    if (heigh>1.8):
        print ("You are in a basketball team!!")
    elif(heigh<1.6):
        print ("You are in a football team!!")
    else:
        print ("You can be in any team you want!!")
    '''
    Output:
    1.8: You are in a basketball team!!
    1.6: You are in a football team!!
    '''

'''
First Task:
1.75: You are in a basketball team!!
1.6: You are in a football team!!
1.45: You are in a football team!!
1.65: You are in a basketball team!!
'''

def School():
    math = int(input("Insert grade in math"))
    computer = int(input("Insert grade  in Computer Science"))
    english = int(input("Insert grade in English"))
    if (math>85  and  computer>85  and  english>85):
        print("You're in a technological scientific reserve classroom")
    elif(math<56  or  computer<56  or  english<56 ):
        print("You are in a regular classroom")
    else:
        print("You're in a mofetclassroom")

'''
Output:
Math: 90 Computer Science: 95 English: 100 
    You're in a technological scientific reserve classroom

Math: 85 Computer Science: 90 English: 85
    You're in a mofetclassroom

Math: 56 Computer Science: 56 English: 56
    You're in a mofet classroom

Math: 45 Computer Science: 90 English: 87
    You are in a regular classroom

Math: 78 Computer Science: 64 English: 72
    You're in a mofet classroom

Math: 45 Computer Science: 88 English: 92
    You are in a regular classroom

A. Yes
B. and means it will return True only if the two conditions are met.
C. or means it will return True if at least one condition is met.

if - Use if to set a condition for an action
else - Same as if with the opposite condition.
elif - Same as else but you can add additional conditions.
'''

def Palindrome():
    num = int(input("Enter a three-digit-number:\n"))
    units = num%10
    hundreds = num//100
    if units == hundreds:
        print("It's a palindrome!!")
    else:
        print("Not a palindrome 8-(")




