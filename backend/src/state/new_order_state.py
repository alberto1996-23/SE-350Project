from backend.src.state.order_state import OrderState
from backend.src.state.submitted_order_state import SubmittedOrderState

class NewOrderState(OrderState):
    def submit(self, order: "Order") -> None:
        """I use this to move a brand-new order into the submitted state."""
        order.change_state(SubmittedOrderState())

    def send_to_kitchen(self, order: "Order") -> None:
        """I use this to block kitchen work until the order is submitted."""
        print("Cannot send a new order to the kitchen before it is submitted.")

    def prepare(self, order: "Order") -> None:
        """I use this to block preparation on a brand-new order."""
        print("Cannot prepare a new order.")

    def mark_ready(self, order: "Order") -> None:
        """I use this to block ready status on a brand-new order."""
        print("Cannot mark a new order as ready.")

    def get_status_name(self) -> str:
        """I use this to label the state as New."""
        return "New"