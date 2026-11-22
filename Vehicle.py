from abc import ABC,abstractmethod # import ABC(Abstarct Main Class)and the abstractmethode
class Vehicle(ABC):                #abstract class Vehicle from ABC
    def __init__(self,name,rental_price_per_day):          #constructor
        self.name=name                                     #public attribute store vehicle name
        self.__rental_price_per_day=rental_price_per_day   #private atribute store vehicle rental price per day

    def get_rental_price(self):                   #getter methode give access to the private attribute
        return self.__rental_price_per_day        #return the private attribute

    @abstractmethod                         #abstract methode, child class must implement it
    def calculate_rent(self,days):               #methode used for claculating rent per days
        pass

    def display_vehicle_details(self):     # normal methode shared by all child classes
        print('vehicle name is:',self.name)   # print the vehicle name
        print('rental price per day:',self.get_rental_price()) #print the vehicle rental price using getter methode