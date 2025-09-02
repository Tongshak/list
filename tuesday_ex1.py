"""
student=0
while student<=10000:
    print(f"student {student:,}")
    student +=1

score = {"Alice": [80,90],"Bob": [70,85],"charlie": [95]}
shouldExecute=True;
while shouldExecute:
    name=input("Enter the students name: ")
    if name.lower() == 'exit':
        print("good bye")
        shouldExecute=False
    else:
        user_score=int(input(f'enter score for{name}:\n'))
        if name in score:
            score[name].append(user_score)
        else:
            score.update({name:[user_score]})
        print(score)
        

a=[1,2,3]
b=a
a.append(4)
print(id(a))
print(id(b))
c=a.copy()
c.append(5)
print(c)
print(id(c))    
"""
students_scores = {
    "Aisha": 95,
    "David": 82,
    "Mary": 99,
    "John": 78,
    "Sarah": 65,
    "Paul": 88,
    "Grace": 100,
    "James": 73,
    "Ruth": 84,
    "Daniel": 90,
    "Michael": 67,
    "Esther": 59,
    "Tunde": 48,
    "Ngozi": 34,
    "Chinedu": 27,
    "Hauwa": 72,
    "Ibrahim": 41,
    "Femi": 53,
    "Victoria": 68,
    "Samuel": 38
}
names = list(students_scores.keys())
a = 0
while a < len(names):
    name = names[a]
    score=students_scores[name]
    if score>=70:
        grade = "A"
    else:
        if score>=60:
            grade="B"
        else:
            if score>=50:
                grade="C"
            else:
                if score>=40:
                    grade="D"
                else:
                    if score>=30:
                        grade="E"
                    else:
                        grade="F"
    print(f"{name}:score = {score},grade = {grade}")
    a +=1

