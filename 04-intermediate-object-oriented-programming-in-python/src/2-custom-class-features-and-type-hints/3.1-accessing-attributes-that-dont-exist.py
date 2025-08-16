class BankAccount:
  def __init__(self, account_number):
    self.account_number = account_number
  
  # Define a magic method to handle references to attribute
  # not in an object's namespace
  def __getattr__(self, name):
    # Output a message to instruct further action
    print(f"""{name} is not defined in BankAccount object.
    	Please define this attribute if needed.""")
    
# Create a BankAccount object, reference routing_number
checking_account = BankAccount("123456")
checking_account.routing_number