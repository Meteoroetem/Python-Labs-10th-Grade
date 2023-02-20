def FirstTask(num):
    cohenCnt = 0
    for i in range(num):
        inp = str(input("What's student #"+str(i+1)+"'s name?"))
        cohenCnt += inp.count("cohen")
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

