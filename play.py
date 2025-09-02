print("welcome to nanribet atm")

customers={"tongshak" : 3137,"nanribet" :1010}
balance=2000
pin=input("please enter your 4 digit pin: ")
amount=int(input("please enter the amount ,you want to withdraw: "))
if amount > 0 and amount <= balance:
    print("transaction successful")
elif amount>balance:
    print("insufficient fund")
else:
    print("good bye")
