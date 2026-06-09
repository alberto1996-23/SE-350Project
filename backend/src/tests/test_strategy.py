from backend.src.order import Order
from backend.src.order_item import OrderItem
from backend.src.menu_item import MenuItem
from backend.src.strategy.dine_in_strategy import DineInStrategy
from backend.src.strategy.take_out_strategy import TakeOutStrategy
from backend.src.strategy.delivery_strategy import DeliveryStrategy, DELIVERY_FEE
from backend.src.strategy.pricing_strategy import SALES_TAX_RATE

def test_dine_in_strategy_calculates_total():
    """I use this to confirm dine-in pricing adds sales tax to the subtotal."""
    order = Order(1, "Dine-In")
    order.set_pricing_strategy(DineInStrategy())
    burger = MenuItem("Pika Patty", "Burger", "Lunch", 5.00)
    fries = MenuItem("Fries", "Side", "Side", 2.00)

    order.add_item(OrderItem(burger, 2))
    order.add_item(OrderItem(fries, 1))

    assert order.calculate_total() == round(12.00 * (1 + SALES_TAX_RATE), 2)


def test_take_out_strategy_calculates_total_with_sales_tax():
    """I use this to confirm take-out pricing adds sales tax to the subtotal."""
    order = Order(1, "Takeout")
    order.set_pricing_strategy(TakeOutStrategy())
    burger = MenuItem("Pika Patty", "Burger", "Lunch", 5.00)

    order.add_item(OrderItem(burger, 2))

    assert order.calculate_total() == round(10.00 * (1 + SALES_TAX_RATE), 2)

def test_delivery_strategy_adds_fee():
    """I use this to confirm delivery pricing adds the delivery fee and sales tax."""
    order = Order(1, "Delivery")
    order.set_pricing_strategy(DeliveryStrategy())
    burger = MenuItem("Pika Patty", "Burger", "Lunch", 5.00)

    order.add_item(OrderItem(burger, 2))

    assert order.calculate_total() == round((10.00 + DELIVERY_FEE) * (1 + SALES_TAX_RATE), 2)