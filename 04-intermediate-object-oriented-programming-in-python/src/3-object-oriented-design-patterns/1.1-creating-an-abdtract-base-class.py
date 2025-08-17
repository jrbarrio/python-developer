# Import the ABC class and abstractmethod decorator from abc
from abc import ABC, abstractmethod

# Define an abstract base class called Company
class Company(ABC):
  # Create an abstract method called create_budget()
  @abstractmethod
  def create_budget(self):
    pass
  
  # Create a concrete method with name hire_employee()
  def hire_employee(self, name):
    print(f"Welcome to the team, {name}!")