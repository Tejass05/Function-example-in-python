name = "xyz"
accno = 1111


def creditamount():
    global amount
    amount = float(input("enter credit amount="))
    global balance
    balance = 0
    balance = balance + amount


def showbalance():
    print(f"{name} and {accno}")
    print(f"Last creadited amount={amount}")
    print(f"Your Current Balance={balance}")


creditamount()
showbalance()