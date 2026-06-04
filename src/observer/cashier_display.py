from observer.order_observer import OrderObserver


class CashierDisplay(OrderObserver):
    def __init__(self, order: "Order"):
        self.__order = order

    def update(self, order: "Order") -> None:
        print(f"[Cashier Display] Order {order.order_id} changed to '{order.status}'.")