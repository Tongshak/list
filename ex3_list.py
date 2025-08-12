"""
noise_makers=[]
print(noise_makers, len(noise_makers))
noise_makers.append("Tongshak")
print(noise_makers, len(noise_makers))
noise_makers.append("Bethel")
print(noise_makers, len(noise_makers))

colours=["blue","black","white","red","yellow","green"]
print(colours, len(colours))
colours.pop()
print(colours, len(colours))
colours.append("orange")
print(colours, len(colours))
colours.insert(1,("orange"))
print(colours)
colours.remove("orange")
#lolours.remove("violet")
print(colours)
colours.insert(10,("violet"))
print(colours)

fruits=["orange","mango","apple","pear"]
print(fruits[0])
print(fruits[-1])
fruits[1]="grapes"
print(fruits)
fruits[0],fruits[-1]=fruits[1],fruits[0]
print(fruits)
fruits[0],fruits[-1]="pear","orange"
print(fruits)
print(fruits[0:3])
fruits=fruits[0:3]
print(fruits)
"""
a=[1,2,3,[4,5,[6,7,[8],9]]]
print(a[3][2][2][0])
print(a[3][2][3])
