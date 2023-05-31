def HowManyLeft(pgNum, totalPgs):
    return totalPgs-pgNum

def Book(author, title, pgNum):
    return f"'{title}', by " + str(author) + f'\n{pgNum}{"*" if pgNum%2 == 0 else "^"}'

def TestBook():
    print(Book(str(input()), str(input()), int(input())))

def FirstAndLastTwice(strA, strB):
    return (str(str(strA)[0]) + str(str(strA)[len(strA)-1]) + "\n"
             + str(str(strB)[0]) + str(str(strA)[len(strB)-1]))

'''
Task #5
 - spng
 - Helo
 - 
 - xyyz

The function prints the first and last two letters in a string 
unless the string's length is less than 2

Task #6
 - ba**le
 - a*rdv*rk
 - goo*le
 - donut

The function replaces letters that are the same as the first with an asterisk
'''

def ReplaceWithLast(string):
    return string[-2:] + string[2:] if len(string) > 4 else string
print(ReplaceWithLast(str(input())))
def Verberize(string):
    if len(string) < 3: return string
    return string + "ly" if string[-3:] == "ing" else string + "ing"