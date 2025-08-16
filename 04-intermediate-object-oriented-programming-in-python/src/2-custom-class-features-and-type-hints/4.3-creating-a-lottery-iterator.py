import random

class Lottery:
  def __init__(self, number_digits):
    self.number_digits = number_digits
    self.counter = 0
    
  def __iter__(self):
    return self
  
  # Check if the number of digits have been reached, or else
  # pull another number
  def __next__(self):
    if self.counter < self.number_digits:
      self.counter += 1
      return random.randint(0, 9)

    raise StopIteration
  
charity_lottery = Lottery(4)

# Announce all four numbers
while True:
  try:
    print(next(charity_lottery))
  
  # Handle the last element of the iterator, print a message
  except StopIteration:
    print("... is the winner!")
    break