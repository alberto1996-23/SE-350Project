from observer.order_observer import OrderObserver


class CustomerDisplay(OrderObserver):
    def __init__(self, order: "Order"):
        self.__order = order

    def update(self, order: "Order") -> None:
        print(f"[Customer Display] Order {order.order_id} is now '{order.status}'.")