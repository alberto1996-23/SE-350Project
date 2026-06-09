from backend.src.state.order_state import OrderState
from backend.src.state.preparing_state import PreparingState

class InKitchenState(OrderState):
    def submit(self, order: "Order") -> None:
        """I use this to block submission once the order is already in progress."""
        print("Order is already beyond submission.")

    def send_to_kitchen(self, order: "Order") -> None:
        """I use this to stop the same order from entering the kitchen twice."""
        print("Order is already in the kitchen.")

    def prepare(self, order: "Order") -> None:
        """I use this to move the kitchen order into preparation."""
        order.change_state(PreparingState())

    def mark_ready(self, order: "Order") -> None:
        """I use this to block ready status until preparation happens first."""
        print("Order must be prepared before it can be ready.")

    def get_status_name(self) -> str:
        """I use this to label the state as In Kitchen."""
        return "In Kitchen"