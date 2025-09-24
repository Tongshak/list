def add_number(num):
    def myinner(x):
        return num(x) + 1
    return myinner



@add_number
def myfunction(x):
    return 10
print(myfunction(1))
    
