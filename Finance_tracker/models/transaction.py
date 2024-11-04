# transaction.py

from datetime import datetime

class Transaction:
    def __init__(self, amount: float, transaction_type: str, description: str = "", date: datetime = None):
        self.amount = amount
        self.transaction_type = transaction_type  # "income" o "expense"
        self.description = description
        self.date = date or datetime.now()

    def is_income(self):
        """Ritorna True se la transazione è un'entrata."""
        return self.transaction_type == "income"

    def is_expense(self):
        """Ritorna True se la transazione è un'uscita."""
        return self.transaction_type == "expense"

    def __str__(self):
        return f"Transaction(amount={self.amount}, type={self.transaction_type}, description={self.description}, date={self.date})"
