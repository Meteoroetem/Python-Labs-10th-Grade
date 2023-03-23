def func():
    n = int(input("Please enter a two digit number: "))
    if (n < 10 and n > -10) or n > 99 or n < -99:
        print("That is not a two digit number!! \n")
        func()
    else:
        units = abs(n) % 10
        tens = (abs(n) - units)/10
        if n > 0:
            print("The number, flipped is", int(units * 10 + tens))
        else:
            print("The number, flipped is", int(-(units * 10 + tens)))

func()
