#list
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
#colours.remove("violet")
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

a=[1,2,3,[4,5,[6,7,[8],9]]]
print(a[3][2][2][0])
print(a[3][2][3])
print(a, len(a))

yusuf=["yusuf",False,9]
print(yusuf[2])
yusuf[-1] +=5
print(yusuf)

y=[1,2,["yusuf",False,"9"]]
print(y[2][2], type(y[2][2]))
print(y[2],type(y[2]))
print(y[2][2],type(y[2][2]))
y[2][2] = int(y[2][2]) +5
#y[2][2] +=5
print(y[2][2],type(y[2][2]))
y[2][2] = str(y[2][2])
print(y[2][2], type(y[2][2]))

#tuple
scores=()
print(scores, type(scores))
a=(10)
print(a, type(a))
b=(1,)
print(b, type(b))
c=1,
print(c, type(c))
noise_makers=("dorcas","bethel","yusuf")
print(noise_makers[0])
#noise_makers[0] = "tk"
print(noise_makers)
noise_makers=list(noise_makers)
noise_makers[0]="TG"
noise_makers=tuple(noise_makers)
print(noise_makers)
a,b,c= noise_makers
print(a)
print(b)
print(c)
kingpin,*others=noise_makers
print(kingpin)
print(others)
*kingpin,others=noise_makers
print(kingpin)
print(others)
"""
#dictionary
e={}
print(type(e))
