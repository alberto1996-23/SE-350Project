from order import Order

class Kitchen:
    def __init__(self):
        self.__active_orders: list[Order] = []

    def get_active_orders(self) -> list[Order]:
        return self.__active_orders

    def receive_order(self, order: Order) -> None:
        self.__active_orders.append(order)
        order.send_to_kitchen()

    def prepare_order(self, order: Order) -> None:
        order.prepare_order()

    def mark_order_ready(self, order: Order) -> None:
        order.mark_ready()