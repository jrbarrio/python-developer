from abc import ABC, abstractmethod

# Create a Product interface
class Product(ABC):
  
  # Define a purchase() abstract method
  @abstractmethod
  def purchase(self, quantity):
    pass
  
  # Create an update_price() abstract method
  @abstractmethod
  def update_price(self, new_price):
    pass