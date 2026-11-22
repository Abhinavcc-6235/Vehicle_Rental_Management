from Vehicle import Vehicle  #import vehicle parent class
class Car(Vehicle):           #car class inherit from vehicle class
    def calculate_rent(self,days): #implements the abstract methode from vehicle
       total= (self.get_rental_price()*days+500)
       return total