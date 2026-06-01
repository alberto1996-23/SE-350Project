from state.order_state import OrderState

class ReadyState(OrderState):
    def submit(self, order: "Order") -> None:
        print("Ready order cannot be submitted again.")

    def send_to_kitchen(self, order: "Order") -> None:
        print("Ready order is already finished in the kitchen.")

    def prepare(self, order: "Order") -> None:
        print("Ready order does not need more preparation.")

    def mark_ready(self, order: "Order") -> None:
        print("Order is already ready.")

    def get_status_name(self) -> str:
        return "Ready"