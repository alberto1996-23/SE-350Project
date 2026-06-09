from backend.src.builder.dine_in_order_builder import DineInOrderBuilder
from backend.src.builder.take_out_order_builder import TakeOutOrderBuilder
from backend.src.builder.delivery_builder import DeliveryOrderBuilder
from backend.src.menu_item import MenuItem

def test_dine_in_builder_builds_dine_in_order():
    """I use this to prove the dine-in builder creates the right order shape."""
    builder = DineInOrderBuilder()
    burger = MenuItem("Pika Patty", "Burger", "Lunch", 5.00)

    builder.add_entree(burger, 2)
    order = builder.build()

    assert order.order_type == "Dine-In"
    assert len(order.items) == 1
    assert order.items[0].quantity == 2

def test_delivery_builder_uses_delivery_type():
    """I use this to prove the delivery builder tags the order as delivery."""
    builder = DeliveryOrderBuilder()
    fries = MenuItem("Fries", "Side", "Side", 2.00)

    builder.add_side(fries, 1)
    order = builder.build()

    assert order.order_type == "Delivery"
    assert len(order.items) == 1