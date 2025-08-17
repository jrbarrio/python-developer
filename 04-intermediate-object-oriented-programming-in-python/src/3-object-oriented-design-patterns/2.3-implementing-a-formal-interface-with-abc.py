from abc import ABC, abstractmethod

class Business(ABC):
  @abstractmethod
  def sell_product(self, product_name, price, quantity):
    pass
  
class Bakery(Business):
  def __init__(self, business_name):
    self.business_name = business_name
  
  # Provide a definition of the sell_product() method 
  def sell_product(self, product_name, price, quantity):
    total_revenue = price * quantity
    print(f"""{self.business_name} sold {quantity} 
          {product_name} for a total of ${total_revenue}""")
    
# Attempt to create a Bakery object
blue_eyed_baker = Bakery("Blue Eyed Baker")