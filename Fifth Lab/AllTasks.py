import sys
sys.path.append('../Python-Labs-10th-Grade')
from UserInterface import UI


def DuplicateLetters(string):
    for ot in string:
        print(ot*3,end="")
    print()
'''
הפונקציה מקבלת משפט ואות ומדפיסה את כמות הפעמים שהאות מופיעה
'''
def PrintMiddle(string):
    if len(string)%2 != 0:
        print(string[len(string)//2])
    else:
        print(string[len(string)//2-1:len(string)//2+1])

def FirstAndLast3Letters(string):
   if len(string) < 3: return "***"
   return string[:3] + string[-3:]

def CountIs(string):
   return string.upper().count(" IS ")

def CountAEIOU(string):
   capStr = str(string).upper()
   return capStr.count("A") + capStr.count("E") + capStr.count("I") + capStr.count("O") + capStr.count("u")

def CapSomeLetters(string):
    newString = ""
    for i in range(len(string)):
        letter = string[i].upper() if i%2 <= 0 else string[i].lower()
        newString = newString + letter
    return newString

def FirstAndLast2Letters(string):
    return string[:2] + string[-2:]

def CensorLetters(string):
    newString = string[0]
    for i in range(1,len(string),1):
        letter = string[i] if string[i].upper() != string[0].upper() else "*"
        newString += letter
    return newString

def SwapLetters():
    inp = str(input('Write two words with a space between: ')).split(' ')
    stringA = inp[0]
    stringB = inp[1]
    result = [stringA[:2] + stringB[2:], stringB[:2] + stringA[2:]]
    print(result[1], result[0])

def Verberize(string):
    if len(string) < 3: return string
    return string + "ly" if string[-3:] == "ing" else string + "ing"

myUI = UI([DuplicateLetters, PrintMiddle, FirstAndLast3Letters,
           CountIs, CountAEIOU, CapSomeLetters, FirstAndLast2Letters,
           CensorLetters, SwapLetters, Verberize])
myUI.UserInterface()