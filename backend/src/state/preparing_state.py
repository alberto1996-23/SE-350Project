from backend.src.state.order_state import OrderState
from backend.src.state.ready_state import ReadyState

class PreparingState(OrderState):
    def submit(self, order: "Order") -> None:
        """I use this to block submission while the order is already being worked on."""
        print("Order is already being worked on.")

    def send_to_kitchen(self, order: "Order") -> None:
        """I use this to block sending an already active order back into the kitchen."""
        print("Order is already in progress in the kitchen.")

    def prepare(self, order: "Order") -> None:
        """I use this to block duplicate preparation calls."""
        print("Order is already being prepared.")

    def mark_ready(self, order: "Order") -> None:
        """I use this to move a prepared order into the ready state."""
        order.change_state(ReadyState())

    def get_status_name(self) -> str:
        """I use this to label the state as Preparing."""
        return "Preparing"