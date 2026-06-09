from backend.src.observer.order_observer import OrderObserver


class CashierDisplay(OrderObserver):
    def __init__(self, order: "Order"):
        """I use this to set up the cashier-facing observer."""
        self.__order = order

    def update(self, order: "Order") -> None:
        """I use this to print the latest order status for the cashier view."""
        print(f"[Cashier Display] Order {order.order_id} changed to '{order.status}'.")