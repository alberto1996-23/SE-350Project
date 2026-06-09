from backend.src.strategy.pricing_strategy import PricingStrategy, apply_sales_tax
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from backend.src.order import Order

class TakeOutStrategy(PricingStrategy):
    def calculate_total(self, order: "Order") -> float:
        """I use this to total a take-out order and add sales tax."""
        subtotal = sum(item.get_subtotal() for item in order.items)
        return apply_sales_tax(subtotal)
