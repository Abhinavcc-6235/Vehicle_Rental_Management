from Vehicle import Vehicle    #import vehicle parent class
class Bike(Vehicle):            #bike class inherit from vehicle
    def calculate_rent(self,days):  #implements the abstract methode from vehicle
        total=(self.get_rental_price()*days+100)
        return total