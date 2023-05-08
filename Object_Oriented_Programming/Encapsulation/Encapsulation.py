class Employee:
    #class Constructor
    def __init__(self, name,salary,project):
        self.name = name
        self.salary = salary
        self.project = project

    def showDetails(self):
        print("The Name is",self.name,"and the salary is",self.salary)

    def work(self):
        print(self.name,"is Working on",self.project)


employee01=Employee("Nitin",50000,"Machine Learning")
employee01.showDetails()
employee01.work()
