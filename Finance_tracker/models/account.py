# account.py

class Account:
    def __init__(self, name: str, status: str = "active", balance: float = 0.0):
        self.name = name
        self.status = status
        self.balance = balance

    def deposit(self, amount: float):
        """Aggiunge fondi al saldo dell'account."""
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"
        return "Deposit amount must be positive"

    def withdraw(self, amount: float):
        """Sottrae fondi dal saldo dell'account, se sufficienti."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        return "Insufficient balance or invalid amount"

    def __str__(self):
        return f"Account(name={self.name}, status={self.status}, balance={self.balance})"
