cars = ['audi', 'bmw', 'subaru', 'toyota']
cars = []

if cars:    #列表或元组判空
    for car in cars:
        if  car == 'bmw':   #区分大小写
            print(car.upper())
        elif car.lower() == 'bmw':  #不区分大小写
            print(car)
        else:
            print(car.title())
else:
    print("List cars is null")

print('audi' in cars)
print('audi' not in cars)

