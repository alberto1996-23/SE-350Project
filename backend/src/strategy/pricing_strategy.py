from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from backend.src.order import Order


SALES_TAX_RATE = 0.07


def apply_sales_tax(subtotal: float) -> float:
    """I use this to add sales tax to a subtotal before returning the final total."""
    return round(subtotal * (1 + SALES_TAX_RATE), 2)

class PricingStrategy(ABC):
    @abstractmethod
    def calculate_total(self, order: "Order") -> float:
        """I use this to define how a strategy should total an order."""
        raise NotImplementedError
        
