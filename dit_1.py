"""
# updating a dictionary
cart={}
dan=cart
dre=cart
jibrin=cart
print(cart, id(cart))
dan.update({"milk": 5})
dre.update({"bread": 2})
jibrin.update({"bama": 1})
print(dan)
print(dre)
print(jibrin)
print(cart)

#use uf conditionals in a list
students=["Tk","TG","Bethel","Dre","Dan","Ben"]
print("tk" in students)
contacts={"abel":700,"aaron":800,"ben":400}
print("jibrin" not in contacts)
"""
# if and else statement
temp=28

if temp <15:
    result="cold"
elif temp >=15 and temp <=25:
    result="warm"
else:
    result="hot"
print(result)



