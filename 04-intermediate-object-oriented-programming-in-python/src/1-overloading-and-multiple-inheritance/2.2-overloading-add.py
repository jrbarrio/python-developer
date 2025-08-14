class Storage:
  def __init__(self, capacity):
    self.capacity = capacity
  
  def __add__(self, other):  # Overload the + operator
    # Create a Storage object with the sum of capacity
    return Storage(self.capacity + other.capacity)

onboard_storage = Storage(128)
external_drive = Storage(64)

# Add the two Storage objects, show the total capacity
total_storage = onboard_storage + external_drive
print(total_storage.capacity)