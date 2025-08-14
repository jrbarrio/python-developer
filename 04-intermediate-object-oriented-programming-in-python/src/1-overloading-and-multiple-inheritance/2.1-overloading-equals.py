class Computer:
  def __init__(self, serial_number):
    self.serial_number = serial_number
  
  # Overload the == operator using a magic method
  def __eq__(self, other):
    # Define equality using serial_number
    return self.serial_number == other.serial_number

# Validate two Computers with the same serial_number are equal
first_computer = Computer("81023762")
second_computer = Computer("81023762")
print(first_computer == second_computer)