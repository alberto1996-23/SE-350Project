from observer.order_observer import OrderObserver


class KitchenDisplay(OrderObserver):
    def __init__(self, order: "Order"):
        self.__order = order

    def update(self, order: "Order") -> None:
        print(f"[Kitchen Display] Order {order.order_id} status updated to '{order.status}'.")