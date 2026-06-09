from backend.src.order import Order

class Kitchen:
    def __init__(self):
        """I use this to keep track of the orders the kitchen is working on."""
        self.__active_orders: list[Order] = []

    def get_active_orders(self) -> list[Order]:
        """I use this to return every order currently in the kitchen."""
        return self.__active_orders

    def receive_order(self, order: Order) -> None:
        """I use this to accept an order and push it into the kitchen state."""
        self.__active_orders.append(order)
        order.send_to_kitchen()

    def prepare_order(self, order: Order) -> None:
        """I use this to tell an order to enter its preparing stage."""
        order.prepare_order()

    def mark_order_ready(self, order: Order) -> None:
        """I use this to tell an order it is ready to be picked up."""
        order.mark_ready()