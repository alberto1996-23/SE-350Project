from state.order_state import OrderState
from state.in_kitchen_state import InKitchenState

class SubmittedOrderState(OrderState):
    def submit(self, order: "Order") -> None:
        print("Order has already been submitted.")

    def send_to_kitchen(self, order: "Order") -> None:
        order.change_state(InKitchenState())

    def prepare(self, order: "Order") -> None:
        print("Order must be in the kitchen before it can be prepared.")

    def mark_ready(self, order: "Order") -> None:
        print("Order cannot be marked ready yet.")

    def get_status_name(self) -> str:
        return "Submitted"