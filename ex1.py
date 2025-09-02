"""
number=float(input("enter number:"))
if number<0:
    print("this is a negative number")
else:
    print("this is a possitive number")


lucky_number = 70
number=int(input("enter your lucky number"))
if number<=0:
    print("lucky number must be a possitive number")
elif number>=0 and number <= 9:
    print("you are almostlucky")
elif number==lucky_number:
    print(f"congrats {number} is the lucky number")

lucky_number=10
try:
   user_number=int(input("enter your lucky number"))
except valueError: 
    if user_number<0:
        print("lucky number must be possitive")
    elif user_number >=0 and user_number <=9:
        print("you are almost lucky")
    elif user_number == lucky_number:
        print(F"congrat{user_number} is the lucky number, you won")
    else:
        print("enter a number from 0 -10")
except valueError:
        print("input must be a number")
"""
word = "Dod"
unique_characters=word[1]
multiple_characters=word[0],[2]
print(word)
print(unique_characters)

word="Dod"
word.
print(word)
