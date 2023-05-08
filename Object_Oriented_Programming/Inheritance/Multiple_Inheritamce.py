class Person:
    def person_data(self,name,age):
        print("Hello from person class")
        print("The name is",name," and this is",age)

class Company:
    def company_data(self,company_name,location):
        print("Hello from company class")
        print("The name is",company_name," and this is",location)

class Employee(Person,Company):
    def employee_data(self,salary,skills):
        print("Hello from employee class")
        print("The salery is",salary," and this is",skills)

emp01 = Employee()
emp01.person_data("Nitin",25)
emp01.company_data("ABCD","Locations")
emp01.employee_data("1000","Data Science")
