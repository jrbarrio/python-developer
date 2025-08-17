from abc import ABC, abstractmethod

# Define a Company abstract base class with a pay_taxes() method
class Company(ABC):
  @abstractmethod
  def pay_taxes(self):
    pass
  
  def report_revenue(self):
    print(f"{self.name} is reporting ${self.revenue} of revenue")

class Manufacturing(Company):
  def __init__(self, name, revenue):
    self.name = name
    self.revenue = revenue

  def pay_taxes(self, tax_rate):
    tax_amount = self.revenue * tax_rate
    print(f"{self.name} is paying ${tax_amount} of taxes")

# Create an instance of the Manufacturing class
m = Manufacturing("Morgan's Manufacturing", 5000)

# Make call to the pay_taxes() method, observe report_revenue()
m.pay_taxes(0.1)
m.report_revenue()