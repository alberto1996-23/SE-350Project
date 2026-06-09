from backend.src.state.order_state import OrderState

class ReadyState(OrderState):
    def submit(self, order: "Order") -> None:
        """I use this to block resubmitting a finished order."""
        print("Ready order cannot be submitted again.")

    def send_to_kitchen(self, order: "Order") -> None:
        """I use this to block sending a finished order back to the kitchen."""
        print("Ready order is already finished in the kitchen.")

    def prepare(self, order: "Order") -> None:
        """I use this to block extra preparation once the order is ready."""
        print("Ready order does not need more preparation.")

    def mark_ready(self, order: "Order") -> None:
        """I use this to block duplicate ready transitions."""
        print("Order is already ready.")

    def get_status_name(self) -> str:
        """I use this to label the state as Ready."""
        return "Ready"