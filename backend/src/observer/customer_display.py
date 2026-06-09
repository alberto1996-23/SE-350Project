from backend.src.observer.order_observer import OrderObserver


class CustomerDisplay(OrderObserver):
    def __init__(self, order: "Order"):
        """I use this to set up the customer-facing observer."""
        self.__order = order

    def update(self, order: "Order") -> None:
        """I use this to print the latest order status for the customer view."""
        print(f"[Customer Display] Order {order.order_id} is now '{order.status}'.")