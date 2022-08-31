"""Classes for melon orders."""

import datetime
import random



class AbstractMelonOrder:   

    def __init__(self, species, qty):
    

        self.species = species
        self.qty = qty
        self.shipped = False

        print(qty)
        if qty > 100:
            raise TooManyMelonsError("No more than 100 melons!")


    def get_base_price(self):

        base_price = random.randint(5,9)

        current_time = datetime.datetime.now() #getting the live hour

        week_day = current_time.weekday() #getting the current day
        current_hour = current_time.hour #getting the current hour
        # current_hour = 9 # testing with rush hour

        #checking if day and time is in between the rush hour 
        if week_day <= 4:

            if current_hour >= 8 and current_hour <= 11:
                base_price = base_price + 4 #incresing the price if it is rush hour

        # print(generate_random_num) test
        return base_price


    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        
        if self.species == "Christmas":
            base_price = base_price * 1.5 #making the new price 1.5 times as much as base price
       
        total = (1 + self.tax) * self.qty * base_price            

        return total   
       

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic" #making it class attribut
    tax = 0.08
        

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super().__init__(species, qty) #acessing parent class
        
        



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international" #making it class attribut
    tax = 0.17
    


    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.country_code = country_code


    def get_total(self):

        total_including_flat_fee = super().get_total()

        if self.qty < 10:
            total_including_flat_fee = total_including_flat_fee + 3

        return total_including_flat_fee    
        

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):

    passed_inspection = False
    tax = 0

    def mark_inspection(self, passed):

        self.passed_inspection = passed

class TooManyMelonsError(ValueError):
    pass




# print(current_time.weekday())
# print(current_time.hour)
melon_gov_order = DomesticMelonOrder(9, 512)
print(melon_gov_order.get_total())