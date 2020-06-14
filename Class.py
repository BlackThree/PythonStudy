class CDog():
    def __init__(self, name, age):
        self.name   = name
        self.age    = age

    def sit(self):
        print(self.name.title() + " is now sitting")

    def rollOver(self):
        print(self.name.title() + " rolled over!")

myDog = CDog("Xiaohui", 8)
myDog.sit()
myDog.rollOver()

#类继承，都是公有继承
class CCar():
    def __init__(self, make, model, year):
        self.make   = make
        self.model  = model
        self.year   = year
        self.odometerReading = 0

    def getDescriptiveName(self):
        longName = str(self.year) + " " + self.make + " " + self.model
        return longName.title()
    
    def readOdometer(self):
        print("This car has " + str(self.odometerReading) + " miles on it.")

    def updateOdometer(self, mileage):
        if mileage >= self.odometerReading:
            self.odometerReading = mileage
        else:
            print("You can't roll back an odometer!")

    def incrementOdometer(self, miles):
        self.odometerReading += miles

class CEletricCar(CCar):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

myTesla = CEletricCar("tesla", "model s", 2020)
print(myTesla.getDescriptiveName())