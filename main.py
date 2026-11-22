from Vehicle import Vehicle # import vehicle parent class
from Bike import Bike       #import  bike class 
from Car import Car         # import car class
print('-------displaying vehicle details---------')

car=Car('benz',2000)        
car.display_vehicle_details()

bike=Bike('yamaha',300)
bike.display_vehicle_details()

print('-------rental charges------------')
car.calculate_rent(3)
print('car rent for 3 days:',car.calculate_rent(3))

b1=bike.calculate_rent(3)
print('bike rent for 3 days:',b1)

print('****************************************')

#OUTPUT
# -------displaying vehicle details---------
# vehicle name is: benz
# rental price per day: 2000
# vehicle name is: yamaha
# rental price per day: 300
# -------rental charges------------
# car rent for 3 days: 6500
# bike rent for 3 days: 1000