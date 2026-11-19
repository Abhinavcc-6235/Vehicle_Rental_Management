from Vehicle import Vehicle
from Bike import Bike
from Car import Car
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