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

