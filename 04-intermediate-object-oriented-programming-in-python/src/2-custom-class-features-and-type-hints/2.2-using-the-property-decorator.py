class BankAccount:
  def __init__(self, email):
    self.email = email
    
  @property
  def email(self):
    return f"Email for this account is: {self._email}"
  
  @email.setter
  def email(self, new_email_address):
    if "@" in new_email_address:
      self._email = new_email_address
    else:
      print("Please make sure to enter a valid email.")
  
  # Define a method to be used when deleting the email attribute
  @email.deleter
  def email(self):
    del self._email
    print("Email deleted, make sure to add a new email!")