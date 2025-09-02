"""
steps=0
while steps <=10:
   
#print(steps,steps!=5)
   steps+=1
   if steps !=5:
       print(steps)

#Task1
odd_number=[]
even_number=[]
steps=1
while steps<=10:
    if steps % 2 ==0:
        even_number.append(steps)
    else:
        odd_number.append(steps)
    steps +=1
print(even_number)
print(odd_number)

numbers=[]
selected=[]
steps=0
while steps<=100:
    if steps % 10 ==0:
        selected.append(steps)
    else:
        numbers.append(steps)
    steps +=10
print(selected)
"""
incrementby10=True
x=10
while x <100:
    if incrementby10:
        x+=10
        print(x)
        incrementby10=False
        else:
            incrementby10:
            x+=5
            print(x)
            incrementby10=False
    else: 
        incrementby10:
        x+=15
        print(x)
        incrementby10=True
