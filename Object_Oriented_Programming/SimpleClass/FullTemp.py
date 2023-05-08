class Snake:
    def __init__(self,name):
        self.name = name

    def modifyName(self,newName):
        self.name=newName


Anacoda1=Snake("Anacoda")
Python1=Snake("Python")


print(Anacoda1.name)
print(Python1.name)