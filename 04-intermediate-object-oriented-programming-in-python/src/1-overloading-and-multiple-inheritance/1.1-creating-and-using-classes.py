class Computer:
  def __init__(self, storage):
    self.storage = storage

  def add_external_drive(self, external_storage):
    self.storage += external_storage
    print(f"Your computer now has {self.storage} GB of storage.")

  @classmethod
  def power_on(cls):
    print("Your computer is starting up!")

my_computer = Computer(512)

# Add an external drive of 256 GB
my_computer.add_external_drive(256)