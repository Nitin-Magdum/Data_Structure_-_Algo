# method overriding using inheritance
class Bird:
    def intro(self):
        print("Birds can fly over the sky")

    def flight(self):
        print("Most of birds can fly")


# First Child class
class Sparrow(Bird):
    def flight(self):
        print("Sparrow can fly")


#  Second Child class 
class Ostrich(Bird):
    def flight(self):
        print("ostrich cannot fly")


bird01 = Bird()
sparrow01= Sparrow()
ostrich01= Ostrich()


# Calling into flight

bird01.intro()
bird01.flight()

sparrow01.intro()
sparrow01.flight()

ostrich01.intro()
ostrich01.flight()