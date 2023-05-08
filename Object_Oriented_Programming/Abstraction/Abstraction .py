from abc import ABC,abstractclassmethod

class ABsclass(ABC):
    def Print(self,x):
        print("Inserted value:", x)
        
    @abstractclassmethod
    def task(self):
        print("THis is inside Abstract")

class test_class(ABsclass):
    def task(self):
        print("Hi, we are in a test class")

class example_class(ABsclass):
    def task(self):
        print("Hi, we are in a example class")

task01=test_class()
task01.task()
task01.Print(5)


example01=example_class()
example01.task()
example01.Print(10)

print("Test is Abstract class?",isinstance(task01,ABsclass))

print("Example is Abstract class?",isinstance(example01,ABsclass))
