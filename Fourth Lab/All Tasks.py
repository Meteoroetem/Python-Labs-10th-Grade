import sys
sys.path.append('../Python-Labs-10th-Grade')
from UserInterface import UI


def FirstTask(num):
    cohenCnt = 0
    for i in range(num):
        inp = str(input("What's student #"+str(i+1)+"'s name?"))
        inpCap = inp.upper()
        cohenCnt += inpCap.count("COHEN")
    print(cohenCnt)

def SecondTask(string):
    strArr = str(string).split(' ')
    print(strArr[0],strArr[len(strArr)-1])

def ThirdTask(string):
    print(string[0] + string[len(string)-1])

def FourthTask(string):
    strArr = str(string).split(' ')
    for word in strArr:
        print(word[0], end="")
    print()


#-------------------------------------------------------------

def TestFirstTask():
    inp = int(input('Write the number of students: '))
    FirstTask(inp)
def SecondTaskTest():
    inp = str(input('Write something: '))
    SecondTask(inp)
def ThirdTaskTest():
    inp = str(input('Write something: '))
    ThirdTask(inp)
def FourthTaskTest():
    inp = str(input('Write something: '))
    FourthTask(inp)


myUI = UI([TestFirstTask,SecondTaskTest,ThirdTaskTest,FourthTaskTest])
myUI.UserInterface()