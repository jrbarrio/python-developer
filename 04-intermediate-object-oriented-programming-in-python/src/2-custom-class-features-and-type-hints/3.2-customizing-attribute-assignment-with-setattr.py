class BankAccount:
  def __init__(self, account_number):
    self.account_number = account_number
  
  def __setattr__(self, name, value):
    if name in ["account_number", "balance"]:
      print(f"{name} is an allowed attribute.")
      self.__dict__[name] = value
    else:
      print(f"Invalid Attribute: {name}")

# Use savings_account and attempt to set attributes
savings_account = BankAccount("12345678")
savings_account.balance = 100
savings_account.beneficiary = "Anna Wu"