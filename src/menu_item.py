class MenuItem:
    def __init__(self, name: str, description: str, category: str, base_price: float):
        self.name = name
        self.description = description
        self.category = category
        self.base_price = base_price

    def get_price(self) -> float:
        return self.base_price

    def get_description(self) -> str:
        return self.description

    def __str__(self) -> str:
        return f"{self.name} ({self.category}) - ${self.base_price:.2f}"