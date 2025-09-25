"""
class numbers:
    def __iter__(self):
        self.number=1
        return self
    def __next__(self):
        a=self. number
        self.number += 1
        return a
my_class = numbers()
foriter = iter(my_class)
print(next(foriter))
print(next(foriter))
print(next(foriter))
print(next(foriter))
print(next(foriter))
"""
class MyCountDown:
    def __init__(self,stop,direction):
        self.stop=stop
        self.direction=direction
    def __iter__(self):
        self.number=1
        return self
    def __next__(self):
        a=self. number
        self.number += 1
        return a
my_class = MyCountDown()
foriter = iter(my_class)
count = MyCountDown
print(next(foriter))
print(next(foriter))
print(next(foriter))
print(next(foriter))
print(next(foriter))