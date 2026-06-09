from backend.src.strategy.pricing_strategy import PricingStrategy, apply_sales_tax
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from backend.src.order import Order


DELIVERY_FEE = 3.50

class DeliveryStrategy(PricingStrategy):
    def calculate_total(self, order: "Order") -> float:
        """I use this to total a delivery order and add the delivery fee."""
        total = sum(item.get_subtotal() for item in order.items)
        return apply_sales_tax(total + DELIVERY_FEE)
