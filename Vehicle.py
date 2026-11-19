from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,name,rental_price_per_day):
        self.name=name
        self.__rental_price_per_day=rental_price_per_day

    def get_rental_price(self):
        return self.__rental_price_per_day   

    @abstractmethod
    def calculate_rent(days):
        pass

    def display_vehicle_details(self):
        print('vehicle name is:',self.name)
        print('rental price per day:',self.get_rental_price())