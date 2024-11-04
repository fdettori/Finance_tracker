# investment.py

class Investment:
    def __init__(self, principal: float, interest_rate: float, duration_years: int, investment_type: str = "stock"):
        self.principal = principal
        self.interest_rate = interest_rate  # Tasso di interesse annuale (es. 0.05 per 5%)
        self.duration_years = duration_years
        self.investment_type = investment_type  # Tipo di investimento, es. "stock", "bond"

    def calculate_return(self):
        """Calcola il valore futuro dell'investimento usando l'interesse composto."""
        return self.principal * (1 + self.interest_rate) ** self.duration_years

    def __str__(self):
        return (f"Investment(principal={self.principal}, interest_rate={self.interest_rate}, "
                f"duration_years={self.duration_years}, type={self.investment_type})")
