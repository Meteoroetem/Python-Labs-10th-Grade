num = int(input("What's your number? "))
digit1 = int(num/100)
digit2 = int((num%100)/10)
digit3 = (num%100)%10
print("Sum of digits: ", digit1+digit2+digit3)
print("Digits swapped: ", digit3*100+digit2*10+digit1)
