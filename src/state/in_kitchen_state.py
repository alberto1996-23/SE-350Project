from state.order_state import OrderState
from state.preparing_state import PreparingState

class InKitchenState(OrderState):
    def submit(self, order: "Order") -> None:
        print("Order is already beyond submission.")

    def send_to_kitchen(self, order: "Order") -> None:
        print("Order is already in the kitchen.")

    def prepare(self, order: "Order") -> None:
        order.change_state(PreparingState())

    def mark_ready(self, order: "Order") -> None:
        print("Order must be prepared before it can be ready.")

    def get_status_name(self) -> str:
        return "In Kitchen"