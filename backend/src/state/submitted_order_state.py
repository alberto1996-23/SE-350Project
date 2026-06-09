from backend.src.state.order_state import OrderState
from backend.src.state.in_kitchen_state import InKitchenState

class SubmittedOrderState(OrderState):
    def submit(self, order: "Order") -> None:
        """I use this to stop an already submitted order from being submitted twice."""
        print("Order has already been submitted.")

    def send_to_kitchen(self, order: "Order") -> None:
        """I use this to move a submitted order into the kitchen state."""
        order.change_state(InKitchenState())

    def prepare(self, order: "Order") -> None:
        """I use this to block preparation until the kitchen receives the order."""
        print("Order must be in the kitchen before it can be prepared.")

    def mark_ready(self, order: "Order") -> None:
        """I use this to block ready status until preparation is finished."""
        print("Order cannot be marked ready yet.")

    def get_status_name(self) -> str:
        """I use this to label the state as Submitted."""
        return "Submitted"