class BankAccount:
  def __init__(self, balance):
    self.balance = balance

  @property
  def balance(self):
    return f"${round(self._balance, 2)}"

  @balance.setter
  def balance(self, new_balance):
    if new_balance > 0:
      self._balance = new_balance

  @balance.deleter
  def balance(self):
    print("Deleting the 'balance' attribute")
    del self._balance

checking_account = BankAccount(100)

# Output the balance of the checking_account object
print(checking_account.balance)

# Set the balance to 150, output the new balance
checking_account.balance = 150
print(checking_account.balance)

# Delete the balance attribute, attempt to print the balance
del checking_account.balance