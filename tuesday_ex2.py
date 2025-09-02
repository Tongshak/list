engine_on=False
car_running=True
print("welcome to Beetle auto car!")
print('available commands: "start","stop","drive","reverse","park"\n')
while car_running:
    command=input("enter command: ")
    if command =="start":
        if engine_on:
            print("engine is already on.")
        else:
            engine_on=True
            print("engine started.")
    elif command == "stop":
        if not engine_on:
            print("engine is already off.")
        else:
            engine_on=False
            print("engine stopped")
    elif command=="drive":
        if engine_on:
            print("beetle is driving")
        else:
            print("cant drive, beetle is already off")
    elif command=="reverse":
        if engine_on:
            print("beetle on reverse")
        else:
            print("cant reverse,engine is off.")
    elif command=="park":
        if engine_on:
            print("cant park while engine is on,stop engine first")
        else:
            print("car parked")
            car_running=False
    else:
        print("unknown command, try again")
