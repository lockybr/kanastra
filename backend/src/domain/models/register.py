import json

class Register:
    def __init__(self, name: str, government_id: int, email: str, debt_amount: int, debt_due_date: str, debt_id: int) -> None:
        self.name = name
        self.government_id = government_id
        self.email = email
        self.debt_amount = debt_amount
        self.debt_due_date = debt_due_date
        self.debt_id = debt_id

    def __str__(self):
        json_class = {
            "name": self.name,
            "government_id": self.government_id,
            "email": self.email,
            "debt_amount": self.debt_amount,
            "debt_due_date": self.debt_due_date,
            "debt_id": self.debt_id
        }
        return json.dumps(json_class)