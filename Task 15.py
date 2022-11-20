budget = int(input("How much money did she have? "))
spendings = int(input("And how much did she spend? "))

if budget - spendings >= 0:
    print("Dana has only", budget-spendings, "shekels left!")
else:
    print("Oh no!! Dana is in a debt of", -(budget-spendings), "shekels!!!")