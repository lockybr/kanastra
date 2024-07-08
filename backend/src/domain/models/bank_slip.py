class BankSlip:
  last_number = 0

  def __init__(self, value: int, due_date: str, payer_name: str) -> None:
    self.value = value
    self.due_date = due_date
    self.payer_name = payer_name
    self.number = self.generate_number()
  
  @classmethod
  def generate_number(cls):
    cls.last_number += 1
    return cls.last_number