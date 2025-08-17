from abc import ABC, abstractmethod

class Company(ABC):
  @abstractmethod
  def create_budget(self):
    pass

  def hire_employee(self, name):
    print(f"Welcome to the team, {name}!")

# Create a class with the name "Technology"
class Technology(Company):
  def __init__(self, name):
    self.name = name

  # Define a create_budget() method
  def create_budget(self, year, expenses):
    for expense, amount in expenses.items():
      print(f"{year} budget for {expense} is {amount}")
  
# Create an instance of the Technology class, call methods
t = Technology("Tina's Tech Advisors")
t.create_budget(2024, {"Salaries": 10000, "Supplies": 500})
t.hire_employee("Christian")