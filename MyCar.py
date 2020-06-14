from Class import CCar  #其它执行语句也会运行

myNewCar = CCar("audi", "a4", 2016)
print(myNewCar.getDescriptiveName())

myNewCar.odometerReading = 23
myNewCar.readOdometer()
