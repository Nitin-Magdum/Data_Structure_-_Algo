class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age= age  #Privet Member


    # Getting age
    def get_age(self):
        return self.__age
    

    # Setting age
    def set_age(self,age):
        self.__age = age

person01 = Person("Nitin",25)

# Getting Privet age for person01
print("Name:",person01.name,"age:",person01.get_age())


# modify age
person01.set_age(26)

print("Name:",person01.name,"age:",person01.get_age())