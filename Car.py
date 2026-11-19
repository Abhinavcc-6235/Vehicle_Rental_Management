from Vehicle import Vehicle
class Car(Vehicle):
    def calculate_rent(self,days):
       total= (self.get_rental_price()*days+500)
       return total