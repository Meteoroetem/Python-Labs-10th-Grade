def func():
    n = int(input("Please enter a two digit number: "))
    if (n < 10 and n > -10) or n > 99 or n < -99:
        print("That is not a two digit number!! \n")
        func()
    else:
        tens = (abs(n) - (abs(n) % 10))/10
        units = abs(n) % 10
        print("The sum of the digits is", int(tens + units))

func()
