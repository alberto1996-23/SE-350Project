from backend.src.order import Order
from backend.src.order_item import OrderItem
from backend.src.menu_item import MenuItem
from backend.src.builder.order_builder import OrderBuilder
from backend.src.strategy.dine_in_strategy import DineInStrategy


class DineInOrderBuilder(OrderBuilder):
    def __init__(self):
        """I use this to start a dine-in order builder with a fresh order."""
        self.currentOrder = self._create_order()

    def _create_order(self) -> Order:
        """I use this to create a new dine-in order with the dine-in strategy."""
        order = Order(1, "Dine-In")
        order.set_pricing_strategy(DineInStrategy())
        return order

    def reset(self) -> None:
        """I use this to clear the builder back to a fresh dine-in order."""
        self.currentOrder = self._create_order()

    def set_order_type(self, order_type: str) -> None:
        """I use this to override the order type if I need to."""
        self.currentOrder.order_type = order_type

    def add_entree(self, item: MenuItem, quantity: int) -> None:
        """I use this to add an entree line item to the current order."""
        self.currentOrder.add_item(OrderItem(item, quantity))

    def add_side(self, item: MenuItem, quantity: int) -> None:
        """I use this to add a side line item to the current order."""
        self.currentOrder.add_item(OrderItem(item, quantity))

    def add_drink(self, item: MenuItem, quantity: int) -> None:
        """I use this to add a drink line item to the current order."""
        self.currentOrder.add_item(OrderItem(item, quantity))

    def add_dessert(self, item: MenuItem, quantity: int) -> None:
        """I use this to add a dessert line item to the current order."""
        self.currentOrder.add_item(OrderItem(item, quantity))

    def build(self) -> Order:
        """I use this to hand back the built dine-in order and reset the builder."""
        built_order = self.currentOrder
        self.reset()
        return built_order
