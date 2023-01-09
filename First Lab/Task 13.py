def func():
    n1 = int(input("What's the first number? "))
    n2 = int(input("What's the second number? "))

    if n1>n2:
        remainder = n1 % n2
        
        print("Remainder: ", remainder, "First number divided by the second number: ", float(n1)/float(n2), "Averege: ", (float(n1)+float(n2))/2)
    else:
        print("The first number must be bigger then the second number \n")
        func()

func()


