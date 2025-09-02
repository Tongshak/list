employer={"sam":{"access level":True},
"tong":{"access level":False}}
i.d_number={"id number1":777888,"id number2":173137}
number=input("enter your employer id number: ")
if number in employer:
    if employer[number]["access level"]:
        info=input("enter name for more info: ")
        if info in i.d_number:
            print(info["id number1"])
        else:
            print("no infomation")
    else:
        print("no access")
else:
    print("user not found")
