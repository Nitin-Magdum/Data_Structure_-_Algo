#parents class
class Vehicle:
    def Vehicle_data(self):
        print("Vehicle Data")

#Car Child Class
class Car(Vehicle):
    def Car_data(self):
        print("Car Data")

#Bike Child Class
class Bike(Vehicle):
    def bike_data(self):
        print("Bike Data")


#object 
car01=Car()
biike01=Bike()
car01.Vehicle_data()
car01.Car_data()
print("================================================================")
biike01.Vehicle_data()
biike01.bike_data()