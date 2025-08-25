users={"samson":{"isstudent":True},
"bethel":{"isstudent":False},
"ben":{"isstudent":True}}
words={"noun":"jos","game":"GTA"}
name=input("enter your name:")
if name in users:
    if users[name]["isstudent"]:
        word=input("enter your word:")
        if word in words:
            print(word["noun"])
        else:
            print("word not found")
    else:
        print("not a student")
else:
    print("user not found")
