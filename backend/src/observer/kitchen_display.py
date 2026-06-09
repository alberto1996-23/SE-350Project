from backend.src.observer.order_observer import OrderObserver


class KitchenDisplay(OrderObserver):
    def __init__(self, order: "Order"):
        """I use this to set up the kitchen-facing observer."""
        self.__order = order

    def update(self, order: "Order") -> None:
        """I use this to print the latest order status for the kitchen view."""
        print(f"[Kitchen Display] Order {order.order_id} status updated to '{order.status}'.")