print("===monthly expenses===")
expenses=0.0
while True:
    value=float (input("enter your amount"))
    if value == -1:
        break
    expenses = expenses + value
    print("total expenses:",expenses)