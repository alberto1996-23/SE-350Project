from order import Order
from order_item import OrderItem
from menu_item import MenuItem
from builder.order_builder import OrderBuilder


class TakeOutOrderBuilder(OrderBuilder):
    def __init__(self):
        self.currentOrder = Order(1, "Takeout")

    def reset(self) -> None:
        self.currentOrder = Order(1, "Takeout")

    def set_order_type(self, order_type: str) -> None:
        self.currentOrder.order_type = order_type

    def add_entree(self, item: MenuItem, quantity: int) -> None:
        self.currentOrder.add_item(OrderItem(item, quantity))

    def add_side(self, item: MenuItem, quantity: int) -> None:
        self.currentOrder.add_item(OrderItem(item, quantity))

    def add_drink(self, item: MenuItem, quantity: int) -> None:
        self.currentOrder.add_item(OrderItem(item, quantity))

    def add_dessert(self, item: MenuItem, quantity: int) -> None:
        self.currentOrder.add_item(OrderItem(item, quantity))

    def build(self) -> Order:
        built_order = self.currentOrder
        self.reset()
        return built_order
